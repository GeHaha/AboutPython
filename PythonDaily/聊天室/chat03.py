from asynchat import async_chat
from asyncore import dispatcher
import asyncore


class ChatSession(async_chat):
    def __init__(self, server, sock, addr):
        async_chat.__init__(self, sock)
        self.server = server
        self.addr = addr
        self.set_terminator('\r\n'.encode())
        self.data = []
        self.push('欢迎进入{}聊天室！\r\n'.format(server.name).encode('GBK'))

    def collect_incoming_data(self, data):
        self.data.append(data.decode())

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)  # 广播当前会话的发言内容到所有会话

    def handle_close(self):  # 定义客户端断开连接的处理方法
        async_chat.handle_close(self)  # 重载超类中的方法
        self.server.disconnect(self)  # 从会话列表中移除当前会话
        self.server.broadcast('{}离开聊天室！\r\n'.format(self.addr[0]))  # 广播当前会话客户端离开信息


class ChatServer(dispatcher):
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket()
        self.bind(('', port))
        self.listen(5)
        self.name = name  # 设置服务器名称
        self.sessions = []

    def disconnect(self, session):  # 定义客户端断开连接的方法
        self.sessions.remove(session)  # 从会话列表移除断开连接的会话

    def broadcast(self, line):  # 定义广播的方法
        for session in self.sessions:  # 遍历所有会话
            session.push('{}\r\n'.format(line).encode('GBK'))  # 向所有会话的客户端推送内容

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self, conn, addr))


if __name__ == '__main__':
    port = 6666
    name = 'Python'
    server = ChatServer(port, name)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print('服务器已关闭！')
