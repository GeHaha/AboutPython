import socket

server = socket.socket()
host = socket.gethostname()
port = 6666
server.connect((host, port))
print(server.recv(1024).decode('GBK'))  # 注意解码以及编码格式
while True:
    name = input('请输入发言内容：')
    server.send('{}\r\n'.format(name).encode())  # 注意将输入内容加上终止符号
