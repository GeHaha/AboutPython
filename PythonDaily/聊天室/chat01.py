import asyncore
from asyncore import dispatcher


class ChatServer(dispatcher):  # 定义聊天服务器类
    def __init__(self, port):  # 重写构造方法
        dispatcher.__init__(self)  # 重载超类的构造方法
        self.create_socket()  # 创建套接字对象
        self.set_reuse_addr()  # 设置地址可重用
        self.bind(('', port))  # 绑定本机地址与端口
        self.listen(5)  # 设置监听连接数

    def handle_accept(self):  # 重写处理客户端连接的方法
        ssl, addr = self.accept()  # 获取服务器端的SSL通道和远程客户端的地址
        ssl.send('您已成功连接服务器！'.encode())  # 发送欢迎信息
        print('连接来自：', addr[0], '端口：', addr[1])  # 显示输出连接的客户端信息


port = 6666  # 设置服务器端口号
server = ChatServer(port)  # 实例化聊天服务器
try:
    asyncore.loop()  # 运行异步循环
except KeyboardInterrupt:  # 捕获键盘中断异常
    print('服务器已被关闭！')
