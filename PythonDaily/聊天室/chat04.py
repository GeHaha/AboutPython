from asyncore import dispatcher
from asynchat import async_chat
import asyncore


class CMDHandler:
    def unknown(self, session, cmd):  # 定义未知命令的处理方法
        session.push('不支持命令：{}\r\n请重新输入！\r\n'.format(cmd).encode('GBK'))  # 向客户端推送错误提示

    def handle(self, session, data):  # 定义命令的处理方法
        if data.strip():  # 判断去除空格后是否还有数据
            parts = data.split(' ', 1)  # 对数据以空格为分割符进行分割（最大分割次数为1次）
            cmd = parts[0]  # 分割后的第1部分为命令
            try:
                line = parts[1].strip()  # 将分割后的第2部分去除空格保存到变量
            except IndexError:  # 如果捕获索引错误
                line = ''  # 设置变量为空值
            method = getattr(self, 'do_' + cmd, None)  # 获取指定名称的方法对象

            try:
                method(session, line)  # 调用获取到的方法对象
            except TypeError:  # 如果捕获类型错误（没有找到方法）
                self.unknown(session, cmd)  # 调用未知命令的处理方法


class Room(CMDHandler):
    def __init__(self, server):  # 定义初始化功能
        self.server = server  # 保存传入的服务器对象
        self.sessions = []  # 初始化会话列表

    def add(self, session):  # 定义单个用户进入房间的处理方法
        self.sessions.append(session)  # 将单个用户的会话添加到会话列表

    def remove(self, session):  # 定义单个用户离开房间的处理方法
        self.sessions.remove(session)  # 从会话列表中移除单个用户的会话

    def broadcast(self, line):  # 定义广播信息的处理方法
        for session in self.sessions:  # 遍历所有的用户会话
            session.push(line.encode('GBK'))  # 向每一个用户会话广播信息（注意编码）

    def do_logout(self, session, line):  # 定义退出命令的处理方法
        raise EndSession  # 抛出结束会话的异常


class EndSession(Exception):
    pass


class CheckInRoom(Room):
    def add(self, session):  # 重写超类的方法
        Room.add(self, session)  # 重载超类的方法
        session.push('欢迎进入{}聊天室！\r\n'.format(self.server.name).encode('GBK'))  # 广播欢迎信息

    def unknown(self, session, cmd):  # 重写位置命令的处理方法
        session.push('请使用命令 <login 用户名> 进行登录！\r\n'.encode('GBK'))  # 推送命令错误的提示

    def do_login(self, session, line):  # 定义登录命令的处理方法
        name = line.strip()  # 数据中命令后方的内容去重空格后作为用户名
        if not name:  # 如果没有内容
            session.push('请输入用户名！\r\n'.encode('GBK'))  # 推送提示
        elif name in self.server.users:  # 如果服务器的用户列表中已有这个用户名
            session.push('用户名 <{}> 已被使用！\r\n'.format(name).encode('GBK'))  # 推送提示
        else:  # 正确输入时
            session.name = name  # 将用户名保存到会话
            session.enter(self.server.main_room)  # 将会话进入到主聊天房间


class ChatRoom(Room):
    def add(self, session):
        self.broadcast('用户 <' + session.name + '> 进入聊天室！\r\n')  # 广播用户进入房间的信息
        Room.add(self, session)  # 重载超类的方法
        self.server.users[session.name] = session  # 向服务器的用户列表添加会话的用户名

    def remove(self, session):
        self.broadcast('用户 <' + session.name + '> 离开聊天室！\r\n')  # 广播用户离开房间的信息
        Room.remove(self, session)  # 重载超类的方法

    def do_say(self, session, line):  # 定义say命令的处理方法
        self.broadcast(session.name + '：' + line + '\r\n')  # 广播用户的发言信息

    def do_look(self, session, line):  # 定义look命令的处理方法
        session.push('当前房间在线用户\r\n'.encode('GBK'))
        session.push('----------------------\r\n'.encode('GBK'))
        for user in self.sessions:  # 遍历所有会话
            session.push('{}\r\n'.format(user.name).encode('GBK'))  # 推送每个会话中的用户名信息

    def do_who(self, session, line):  # 定义who命令的处理方法
        session.push('当前服务器在线用户\r\n'.encode('GBK'))
        session.push('----------------------\r\n'.encode('GBK'))
        for user in self.server.users:  # 遍历服务器用户列表
            session.push('{}\r\n'.format(user).encode('GBK'))  # 推送服务器中所有的用户名信息


class CheckOutRoom(Room):
    def add(self, session):  # 重写进入房间的方法
        try:
            del self.server.users[session.name]  # 从服务器用户列表中移除当前会话的用户名
        except KeyError:
            pass


class ChatSession(async_chat):
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server  # 保存传入服务器对象
        self.set_terminator('\r\n'.encode())
        self.data = []
        self.name = None  # 创建会话的用户名变量
        self.enter(CheckInRoom(server))  # 将当前会话添加到登录的房间

    def enter(self, room):  # 定义进入房间的方法
        try:
            current = self.room  # 获取当前会话的房间
        except AttributeError:  # 如果当前会话没有在任何房间
            pass
        else:  # 如果当前会话没有在某个房间
            current.remove(self)  # 从当前会话所在的房间移除当前会话
        self.room = room  # 设置当前会话的房间为传入的房间
        room.add(self)  # 传入的房间添加当前会话

    def collect_incoming_data(self, data):
        self.data.append(data.decode())

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self, line)  # 处理客户端发来的数据
        except EndSession:  # 捕获结束会话异常
            self.handle_close()  # 调用关闭连接的处理方法

    def handle_close(self):  # 重写关闭连接的处理方法
        async_chat.handle_close(self)  # 重载超类的方法
        self.enter(CheckOutRoom(self.server))  # 将当前会话进入退出登记的房间


class ChatSever(dispatcher):
    def __init__(self, name, port):
        dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name  # 保存传入的聊天室服务器名称
        self.users = {}  # 初始化服务器用户列表
        self.main_room = ChatRoom(self)  # 设定主聊天房间

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)  # 将服务器对象和连接对象传入会话对象


if __name__ == '__main__':
    name = '心动'
    port = 6666
    server = ChatSever(name, port)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print('服务器已关闭！')
