import os
import sys
import time
import datetime
import calendar
import re
import hmac
import base64
import logging
import traceback
import escape
import stat
import email.utils
import mimetypes
import hashlib
import urlparse
import webob
import webob.exc as webob_exc
import Cookie
import template
import binascii
import uuid
from pv import i18n as locale
import functools


_RE_FIND_GROUPS = re.compile(r'''\{(\w+)(?::([^}]+))?\}''', re.VERBOSE)


def template_to_regex(template):
    pattern = ""
    last_pos = 0
    for match in _RE_FIND_GROUPS.finditer(template):
        pattern += re.escape(template[last_pos:match.start()])
        var_name = match.group(1)
        expr = match.group(2) or '[^/]+'
        expr = '(?P<%s>%s)' % (var_name, expr)
        pattern += expr 
        last_pos = match.end()
    #pattern += re.escape(template[last_pos:])
    pattern += template[last_pos:]
    pattern = '^%s$' % pattern
    return pattern

def _utf8(s):
    if isinstance(s, unicode):
        return s.encode("utf-8")
    assert isinstance(s, str)
    return s

def _unicode(s):
    if isinstance(s, str):
        try:
            return s.decode("utf-8")
        except UnicodeDecodeError:
            raise webob_exc.HTTPError
    assert isinstance(s, unicode)
    return s


class LazyLoader(object):
    def __init__(self, import_name):
        self.import_name = import_name
        self.obj = None   
  
    def __call__(self, application, **kwargs):
        if not self.obj or application.settings.get('debug'):
            try:
                self.obj = self._isstring(self.import_name)(application, **kwargs)
            except Exception:
                raise
                kwargs.update({'code': 501})
                self.obj = ErrorHandler(application, **kwargs)
        return self.obj
    
    def _isstring(self, import_name):
        try:
            if '.' in import_name:
                module, obj = import_name.rsplit('.', 1)
            else:
                return __import__(import_name)
            if isinstance(obj, unicode):
                obj = obj.encode('utf-8')
            return getattr(__import__(module, None, None, [obj]), obj)
        except (ImportError, AttributeError):
            raise


class RequestHandler(object):
    _SUPPORTED_METHODS = set(['get', 'post', 'put', 'head', 'delete'])   
    
    def __init__(self, application, **options):
        self.application = application
        self.options = options
        self._auto_finish = True
    
    def __call__(self, request=None, **kwargs):
        assert request
        self.request = request
        self.response = webob.Response(request=self.request,
                                  conditional_response=True,)
        self._finished = False
        self._write_buffer = []
        if hasattr(self, '_cookies'):
            del self._cookies
        
        # @todo: Bunu her defasinda yuklemeye gerek var mi? 
        if self.options.get('translate'):
            locale.load_translations(self.application.settings.get('translations_path'))

        try:
            # If XSRF cookies are turned on, reject form submissions without
            # the proper cookie
            if self.request.method == "POST" and \
               self.application.settings.get("xsrf_cookies"):
                self.check_xsrf_cookie()
            self.prepare()
            self._handle(**kwargs)
            if self._auto_finish and not self._finished:
                self.finish()
        except Exception, e:
            self._handle_request_exception(e)
        
        assert self._finished
        return self.response

    @property
    def settings(self):
        return self.application.settings
    
    _ARG_DEFAULT = []
    def get_argument(self, name, default=_ARG_DEFAULT, strip=True):
        """Returns the value of the argument with the given name.

        If default is not provided, the argument is considered to be
        required, and we throw an HTTP 404 exception if it is missing.

        The returned value is always unicode.
        """
        values = self.request.arguments.get(name, None)
        if values is None:
            if default is self._ARG_DEFAULT:
                raise webob_exc.HTTPFailedDependency
            return default
        # Get rid of any weird control chars
        value = re.sub(r"[\x00-\x08\x0e-\x1f]", " ", values[-1])
        value = _unicode(value)
        if strip: value = value.strip()
        return value

    def write(self, chunk):
        """Writes the given chunk to the output buffer.

        To write the output to the network, use the flush() method below.

        If the given chunk is a dictionary, we write it as JSON and set
        the Content-Type of the response to be text/javascript.
        """
        assert not self._finished
        if isinstance(chunk, dict):
            chunk = escape.json_encode(chunk)
            self.set_header("Content-Type", "text/javascript; charset=UTF-8")
        chunk = _utf8(chunk)
        self._write_buffer.append(chunk)

    def finish(self, chunk=None):
        """Finishes this response, ending the HTTP request."""
        assert not self._finished
        if chunk: self.write(chunk)

        if self.response.status_int == 200 and self.request.method == "GET":
            hasher = hashlib.sha1()
            for part in self._write_buffer:
                hasher.update(part)
            etag = '"%s"' % hasher.hexdigest()
            inm = self.request.headers.get("If-None-Match")
            if inm and inm.find(etag) != -1:
                self._write_buffer = []
                self.response.status_int = 304 
            else:
                self.set_header("Etag", etag)

        self.response.body = "".join(self._write_buffer)
        self._finished = True

    def redirect(self, url, permanent=False):
        url = re.sub(r"[\x00-\x20]+", "", _utf8(url))
        self.response.status = '301 Moved Permanently' if permanent else '302 Moved Temporarily'
        absolute_url = urlparse.urljoin(self.request.uri, url)
        self.response.headers['Location'] = _utf8(absolute_url)
        self._write_buffer = []
        self.finish()

    def require_setting(self, name, feature="this feature"):
        """Raises an exception if the given app setting is not defined."""
        if not self.application.settings.get(name):
            raise Exception("You must define the '%s' setting in your "
                            "application to use %s" % (name, feature))

    def static_url(self, path):
        self.require_setting("static_path", "static_url")
        if not hasattr(RequestHandler, "_static_hashes"):
            RequestHandler._static_hashes = {}
        hashes = RequestHandler._static_hashes
        if path not in hashes:
            try:
                f = open(os.path.join(
                    self.application.settings["static_path"], path))
                hashes[path] = hashlib.md5(f.read()).hexdigest()
                f.close()
            except:
                logging.error("Could not open static file %r", path)
                hashes[path] = None
        base = self.request.protocol + "://" + self.request.host \
            if getattr(self, "include_host", False) else ""
        if hashes.get(path):
            return base + "/static/" + path + "?v=" + hashes[path][:5]
        else:
            return base + "/static/" + path

    def prepare(self):
        pass
      
    def _handle(self, **kwargs):
        method_name = self.request.method.lower()
        method = getattr(self, method_name, None)
        if method_name not in self._SUPPORTED_METHODS or not method:
            raise webob_exc.HTTPMethodNotAllowed
        method(**kwargs)

    def _request_summary(self):
        return self.request.method + " " + self.request.uri + " (" + \
            self.request.remote_addr + ")"

    def _handle_request_exception(self, e):
        if isinstance(e, webob_exc.WSGIHTTPException):
            self.send_error(code=e.status_int, explanation=e.explanation)
        else:
            logging.error("Uncaught exception %s\n%r", self._request_summary(),
                          self.request, exc_info=e)
            lines = ''
            if self.application.settings.get('debug'):
                lines = ''.join(traceback.format_exception(*sys.exc_info()))
            self.send_error(500, traceback=lines)

    def send_error(self, code=500, explanation='Oops!', traceback=''):
        self.response.status_int = code
        self._write_buffer = []
        self.finish(self.get_error_html(code, explanation, traceback))

    def get_error_html(self, status_code, explanation='', traceback=''):
        if len(traceback) > 0:
            traceback = "<pre>%s</pre" % traceback
        return "<html><title>%(code)d %(message)s</title><style type='text/css'>" \
            "html, body { font-family:Arial, Helvetica, serif; padding: 5px; color: #666; background-color: #fff; } " \
            "p { font-size: 25px; } .status { color: #ddd; } pre { background-color: #ffe; " \
            "font-size: 16px; line-height: 1.3em; padding: 10px; color: #111; }" \
            "</style><body><p><span class='status'>" \
            "%(code)d %(message)s</span><br />" \
            "%(explanation)s <br />&mdash;</p>" \
            "%(traceback)s</body></html>" % {
            "code": status_code,
            "message": webob.util.status_reasons[status_code],
            "explanation": explanation,
            "traceback": traceback,}

    def set_header(self, name, value):
        """Sets the given response header name and value.

        If a datetime is given, we automatically format it according to the
        HTTP specification. If the value is not a string, we convert it to
        a string. All header values are then encoded as UTF-8.
        """
        if isinstance(value, datetime.datetime):
            t = calendar.timegm(value.utctimetuple())
            value = email.utils.formatdate(t, localtime=False, usegmt=True)
        elif isinstance(value, int) or isinstance(value, long):
            value = str(value)
        else:
            value = _utf8(value)
            # If \n is allowed into the header, it is possible to inject
            # additional headers or split the request. Also cap length to
            # prevent obviously erroneous values.
            safe_value = re.sub(r"[\x00-\x1f]", " ", value)[:4000]
            if safe_value != value:
                raise ValueError("Unsafe header value %r", value)
        self.response.headers[name] = value
    
    # Cookies

    @property
    def cookies(self):
        """A dictionary of Cookie.Morsel objects."""
        if not hasattr(self, "_cookies"):
            self._cookies = Cookie.BaseCookie()
            if "Cookie" in self.request.headers:
                try:
                    self._cookies.load(self.request.headers["Cookie"])
                except:
                    self.clear_all_cookies()
        return self._cookies

    def clear_cookie(self, name, path="/", domain=None):
        """Deletes the cookie with the given name."""
        self.response.delete_cookie(name, path, domain)

    def clear_all_cookies(self):
        """Deletes all the cookies the user sent with this request."""
        for name in self.cookies.iterkeys():
            self.clear_cookie(name)

    def set_cookie(self, name, value, **kwargs):
        name = _utf8(name)
        value = _utf8(value)
        if re.search(r"[\x00-\x20]", name + value):
            # Don't let us accidentally inject bad stuff
            raise ValueError("Invalid cookie %r: %r" % (name, value))
        self.response.set_cookie(name, value, **kwargs)

    def unset_cookie(self, key):
        """Unset a cookie with the given name (remove it from the response)."""
        self.response.unset_cookie(key)

    def get_cookie(self, name, default=None):
        """Gets the value of the cookie with the given name, else default."""
        if name in self.cookies:
            return self.cookies[name].value
        return default

    def set_secure_cookie(self, key, value, **kwargs):
        timestamp = str(int(time.time()))
        value = base64.b64encode(value)
        signature = self.cookie_signature(value, timestamp)
        self.set_cookie(key, "|".join([value, timestamp, signature]), **kwargs)
    
    def get_secure_cookie(self, key):
        value = self.get_cookie(key, None)
        if not value: return None
        parts = value.split("|")
        if len(parts) != 3: return None
        if self.cookie_signature(parts[0], parts[1]) != parts[2]:
            logging.warning("Invalid cookie signature %r", value)
            return None
        timestamp = int(parts[1])
        if timestamp < time.time() - 30 * 86400:
            logging.warning("Expired cookie %r", value)
            return None
        try:
            return base64.b64decode(parts[0]).strip()
        except:
            return None
    
    def cookie_signature(self, *parts):
        self.require_setting("cookie_secret", "secure cookies")
        hash = hmac.new(self.application.settings["cookie_secret"],
                        digestmod=hashlib.sha1)
        for part in parts: hash.update(part)
        return hash.hexdigest()
    
    # Localization
    
    @property
    def locale(self):
        """The local for the current session.

        Determined by either get_user_locale, which you can override to
        set the locale based on, e.g., a user preference stored in a
        database, or get_browser_locale, which uses the Accept-Language
        header.
        """
        if not hasattr(self, "_locale"):
            self._locale = self.get_user_locale()
            if not self._locale:
                self._locale = self.get_browser_locale()
                assert self._locale
        return self._locale
            
    def get_user_locale(self):
        """Override to determine the locale from the authenticated user.

        If None is returned, we use the Accept-Language header.
        """
        return None

    def get_browser_locale(self, default="en_US"):
        """Determines the user's locale from Accept-Language header.

        See http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4
        """
        if "Accept-Language" in self.request.headers:
            languages = self.request.headers["Accept-Language"].split(",")
            locales = []
            for language in languages:
                parts = language.strip().split(";")
                if len(parts) > 1 and parts[1].startswith("q="):
                    try:
                        score = float(parts[1][2:])
                    except (ValueError, TypeError):
                        score = 0.0
                else:
                    score = 1.0
                locales.append((parts[0], score))
            if locales:
                locales.sort(key=lambda (l, s): s, reverse=True)
                codes = [l[0] for l in locales]
                return locale.get(*codes)
        return locale.get(default)

    # Templates

    def render(self, template_name, **kwargs):
        """Renders the template with the given arguments as the response."""
        html = self.render_string(template_name, **kwargs)
        self.finish(html)

    def render_string(self, template_name, **kwargs):
        """Generate the given template with the given arguments.

        We return the generated string. To generate and write a template
        as a response, use render() above.
        """
        # If no template_path is specified, use the path of the calling file
        template_path = self.application.settings.get("template_path")
        if not template_path:
            frame = sys._getframe(0)
            web_file = frame.f_code.co_filename
            while frame.f_code.co_filename == web_file:
                frame = frame.f_back
            template_path = os.path.dirname(frame.f_code.co_filename)
        if not getattr(RequestHandler, "_templates", None):
            RequestHandler._templates = {}
        if template_path not in RequestHandler._templates:
            RequestHandler._templates[template_path] = template.Loader(
                template_path)
        t = RequestHandler._templates[template_path].load(template_name)
        args = dict(
            handler=self,
            request=self.request,
            static_url=self.static_url,
            locale=self.locale,
            _=self.locale.translate,
            xsrf_form_html=self.xsrf_form_html,
            current_user=self.current_user,
        )
        args.update(kwargs)
        return t.generate(**args)

    def head(self, **kwargs):
        method = getattr(self, 'get', None)
        if not method:
            raise webob_exc.HTTPMethodNotAllowed
        method(**kwargs)
        self._write_buffer = []

    # Authentication
    
    @property
    def current_user(self):
        """The authenticated user for this request.

        Determined by either get_current_user, which you can override to
        set the user based on, e.g., a cookie. If that method is not
        overridden, this method always returns None.

        We lazy-load the current user the first time this method is called
        and cache the result after that.
        """
        if not hasattr(self, "_current_user"):
            self._current_user = self.get_current_user()
        return self._current_user

    def get_current_user(self):
        """Override to determine the current user from, e.g., a cookie."""
        return None

    def get_login_url(self):
        # @todo: Bu ne is?
        """Override to customize the login URL based on the request.

        By default, we use the 'login_url' application setting.
        """
        self.require_setting("login_url", "@tornado.web.authenticated")
        return self.application.settings["login_url"]

    # XSRF

    @property
    def xsrf_token(self):
        """The XSRF-prevention token for the current user/session.

        To prevent cross-site request forgery, we set an '_xsrf' cookie
        and include the same '_xsrf' value as an argument with all POST
        requests. If the two do not match, we reject the form submission
        as a potential forgery.

        See http://en.wikipedia.org/wiki/Cross-site_request_forgery
        """
        if not hasattr(self, "_xsrf_token"):
            token = self.get_cookie("_xsrf")
            if not token:
                token = binascii.b2a_hex(uuid.uuid4().bytes)
                max_age = str(86400*30) if self.current_user else None
                max_age = None
                self.set_cookie("_xsrf", token, max_age=max_age)
            self._xsrf_token = token
        return self._xsrf_token

    def check_xsrf_cookie(self):
        """Verifies that the '_xsrf' cookie matches the '_xsrf' argument.

        To prevent cross-site request forgery, we set an '_xsrf' cookie
        and include the same '_xsrf' value as an argument with all POST
        requests. If the two do not match, we reject the form submission
        as a potential forgery.

        See http://en.wikipedia.org/wiki/Cross-site_request_forgery
        """
        token = self.get_argument("_xsrf", None)
        
        if not token:
            # '_xsrf' argument missing from POST.
            raise webob_exc.HTTPForbidden
        if self.xsrf_token != token:
            # XSRF cookie does not match POST argument.
            raise webob_exc.HTTPForbidden

    def xsrf_form_html(self):
        """An HTML <input/> element to be included with all POST forms.

        It defines the _xsrf input value, which we check on all POST
        requests to prevent cross-site request forgery. If you have set
        the 'xsrf_cookies' application setting, you must include this
        HTML within all of your HTML forms.

        See check_xsrf_cookie() above for more information.
        """
        return '<input type="hidden" name="_xsrf" value="' + \
            escape.xhtml_escape(self.xsrf_token) + '"/>'


class ErrorHandler(RequestHandler):
    def __init__(self, application, **options):
        self.options = options
        RequestHandler.__init__(self, application, **options)

    def prepare(self):
        code = self.options.get('code')
        if not code:
            raise Exception('ErrorHandler needs a status code.')        
        raise webob_exc.status_map[code]()


class RedirectHandler(RequestHandler):
    """Redirects the client to the given URL for all GET requests.

    You should provide the keyword argument "url" to the handler, e.g.:

        application = web.Application([
            (r"/oldpath", web.RedirectHandler, {"url": "/newpath"}),
        ])
    """
    def __init__(self, application, **options):
        self.options = options
        RequestHandler.__init__(self, application, **options)
        self._url = options.get('url', None)
        self._permanent = options.get('permanent', False)
        
    def get(self):
        self.redirect(self._url, permanent=self._permanent)


class StaticFileHandler(RequestHandler):
    def __init__(self, application, path):
        RequestHandler.__init__(self, application)
#       self.root = os.path.abspath(path) + "/" # Win'de "/" koyunca get'in ilk kosulu saglanamiyor.
        self.root = os.path.abspath(path)
    
    def head(self, **kwargs):
        self.get(kwargs.get('file'), include_body=False)
    
    def get(self, **kwargs):
        path = kwargs.get('file')
        abspath = os.path.abspath(os.path.join(self.root, path))
        if not abspath.startswith(self.root):
            if self.application.settings.get('debug'):
                logging.warning("%s is not in root static directory" % path)
            raise webob_exc.HTTPForbidden
        if not os.path.exists(abspath):
            raise webob_exc.HTTPNotFound
        if not os.path.isfile(abspath):
            if self.application.settings.get('debug'):
                logging.warning("%s is not a file" % path)
            raise webob_exc.HTTPNotFound

        # Check the If-Modified-Since, and don't send the result if the
        # content has not been modified
        stat_result = os.stat(abspath)
        modified = datetime.datetime.fromtimestamp(stat_result[stat.ST_MTIME])
        ims_value = self.request.headers.get("If-Modified-Since")
        if ims_value is not None:
            date_tuple = email.utils.parsedate(ims_value)
            if_since = datetime.datetime.fromtimestamp(time.mktime(date_tuple))
            if if_since >= modified:
                self.response.status_int = 304
                return

        self.set_header("Last-Modified", modified)
        self.set_header("Content-Length", stat_result[stat.ST_SIZE])
        if "v" in self.request.arguments:
            self.set_header("Expires", datetime.datetime.utcnow() + \
                                       datetime.timedelta(days=365*10))
            self.set_header("Cache-Control", "max-age=" + str(86400*365*10))
        else:
            self.set_header("Cache-Control", "public")
        
        mime_type, encoding = mimetypes.guess_type(abspath)
        if mime_type:
            self.set_header("Content-Type", mime_type)
        else:
            self.set_header('Content-Type', 'application/unknown')

        if not kwargs.get('include_body', True):
            return
        
        file = open(abspath, "rb")
        try:
            self.write(file.read())
        finally:
            file.close()


class Application(object):
    def __init__(self, url_mappings=None, **settings):
        self.handlers = []
        self.settings = settings
        
        if self.settings.get("static_path"):
            path = self.settings["static_path"]
            url_mappings = list(url_mappings or [])
            url_mappings.extend([
                ("/static/{file}", "pv.web.StaticFileHandler", dict(path=path)),
                ("/{file:(favicon.ico)}", "pv.web.StaticFileHandler", dict(path=path)),
                ("/{file:(robots.txt)}", "pv.web.StaticFileHandler", dict(path=path)),
            ])
        
        for url_mapping in url_mappings:
            assert len(url_mapping) in (2, 3)
            pattern = template_to_regex(url_mapping[0])
            handler = LazyLoader(url_mapping[1])
            if len(url_mapping) == 3:
                kwargs = url_mapping[2]
            else:
                kwargs = {}
            self.handlers.append((re.compile(pattern), handler, kwargs))
            
        # Reload modules here.
        
    def __call__(self, request):
        handler = None
        args = {}
        for pattern, handler_class, options in self.handlers:
            match = pattern.match(request.path)
            if match:
                handler = handler_class(self, **options)
                args = match.groupdict()
                break

        if not handler:
            args.update({'code': 404})
            handler = ErrorHandler(self, **args)

        if self.settings.get("debug"):
            RequestHandler._templates = None
            RequestHandler._static_hashes = {}

        response = handler(request=request,
                           **args)
        return response


def removeslash(method):
    """Use this decorator to remove trailing slashes from the request path.

    For example, a request to '/foo/' would redirect to '/foo' with this
    decorator. Your request handler mapping should use a regular expression
    like r'/foo/*' in conjunction with using the decorator.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.request.path.endswith("/"):
            if self.request.method == "GET":
                uri = self.request.path.rstrip("/")
                if self.request.query: uri += "?" + self.request.query
                self.redirect(uri)
                return
            raise webob_exc.HTTPNotFound
        return method(self, *args, **kwargs)
    return wrapper


def addslash(method):
    """Use this decorator to add a missing trailing slash to the request path.

    For example, a request to '/foo' would redirect to '/foo/' with this
    decorator. Your request handler mapping should use a regular expression
    like r'/foo/?' in conjunction with using the decorator.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.request.path.endswith("/"):
            if self.request.method == "GET":
                uri = self.request.path + "/"
                if self.request.query: uri += "?" + self.request.query
                self.redirect(uri)
                return
            raise webob_exc.HTTPNotFound
        return method(self, *args, **kwargs)
    return wrapper
