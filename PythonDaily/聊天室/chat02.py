import asyncore
from asyncore import dispatcher
from asynchat import async_chat


class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator('\r\n'.encode())  # 设置数据的终止符号
        self.data = []  # 创建数据列表
        self.push('欢迎进入聊天室！'.encode('GBK'))  # 向单个客户端发送欢迎信息

    def collect_incoming_data(self, data):  # 重写处理客户端发来数据的方法
        self.data.append(data.decode())  # 将客户端发来的数据添加到数据列表

    def found_terminator(self):  # 重写发现数据中终止符号时的处理方法
        line = ''.join(self.data)  # 将数据列表中的内容整合为一行
        self.data = []  # 清空数据列表
        print(line)  # 显示客户端输出发来的内容


class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        ssl, addr = self.accept()
        self.sessions.append(ChatSession(ssl))  # 将新的用户连接会话添加到会话列表


port = 6666
server = ChatServer(port)
try:
    asyncore.loop()
except KeyboardInterrupt:
    print('服务器已被关闭！')
