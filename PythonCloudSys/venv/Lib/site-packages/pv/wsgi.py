import re
import web
import webob
import cgi
import logging


_CHARSET_RE = re.compile(r';\s*charset=([^;\s]*)', re.I)


class Request(webob.Request):
    request_body_tempfile_limit = 0

    def __init__(self, environ):
        match = _CHARSET_RE.search(environ.get('CONTENT_TYPE', ''))
        if match:
            charset = match.group(1).lower()
        else:
            charset = 'utf-8'
        
        webob.Request.__init__(self, environ, charset=charset,
                               unicode_errors= 'ignore', decode_param_names=True)
        
        self.arguments = {}
        self.uri = self.path
        self.query = environ.get("QUERY_STRING", "")
        
        self.protocol = environ["wsgi.url_scheme"]
        if self.query:
            self.uri += "?" + self.query
            arguments = cgi.parse_qs(self.query)
            for name, values in arguments.iteritems():
                values = [v.encode('utf-8') for v in values if v]
                if values: self.arguments[name] = values
        
        # Parse request body
        self.files = {}
        content_type = self.headers.get("Content-Type", "")
        if content_type.startswith("application/x-www-form-urlencoded"):
            for name, values in cgi.parse_qs(self.body).iteritems():
                self.arguments.setdefault(name, []).extend(values)
        elif content_type.startswith("multipart/form-data"):
            boundary = content_type[30:]
            if boundary: self._parse_mime_body(boundary)
        

    def full_url(self):
        return self.protocol + "://" + self.host + self.uri

    def _parse_mime_body(self, boundary):
        if self.body.endswith("\r\n"):
            footer_length = len(boundary) + 6
        else:
            footer_length = len(boundary) + 4
        parts = self.body[:-footer_length].split("--" + boundary + "\r\n")
        for part in parts:
            if not part: continue
            eoh = part.find("\r\n\r\n")
            if eoh == -1:
                logging.warning("multipart/form-data missing headers")
                continue
            headers = self.headers
            name_header = headers.get("Content-Disposition", "")
        
            if not name_header.startswith("form-data;") or \
               not part.endswith("\r\n"):
                logging.warning("Invalid multipart/form-data")
                continue
            value = part[eoh + 4:-2]
            name_values = {}
            for name_part in name_header[10:].split(";"):
                name, name_value = name_part.strip().split("=", 1)
                name_values[name] = name_value.strip('"').decode("utf-8")
            if not name_values.get("name"):
                logging.warning("multipart/form-data value missing name")
                continue
            name = name_values["name"]
            if name_values.get("filename"):
                ctype = headers.get("Content-Type", "application/unknown")
                self.files.setdefault(name, []).append(dict(
                    filename=name_values["filename"], body=value,
                    content_type=ctype))
            else:
                self.arguments.setdefault(name, []).append(value)

    def get(self, argument_name, default_value='', allow_multiple=False):
        param_value = self.get_all(argument_name)
        if allow_multiple:
            return param_value
        else:
            if len(param_value) > 0:
                return param_value[0]
            else:
                return default_value

    def get_all(self, argument_name):
        if self.charset:
            argument_name = argument_name.encode(self.charset)
        param_value = self.params.getall(argument_name)
        for i in xrange(len(param_value)):
            if isinstance(param_value[i], cgi.FieldStorage):
                param_value[i] = param_value[i].value
        return param_value

    def arguments(self):
        return list(set(self.params.keys()))

    def get_range(self, name, min_value=None, max_value=None, default=0):
        try:
            value = int(self.get(name, default))
        except ValueError:
            value = default
        if max_value != None:
            value = min(value, max_value)
        if min_value != None:
            value = max(value, min_value)
        return value


class WSGIApplication(web.Application):
    def __init__(self, url_mappings=None, **settings):
        web.Application.__init__(self, url_mappings, **settings)

    def __call__(self, environ, start_response):
        response = web.Application.__call__(self, Request(environ))
        return response(environ, start_response)