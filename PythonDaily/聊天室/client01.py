import socket

server = socket.socket()
host = socket.gethostname()
port = 6666
server.connect((host, port))
print(server.recv(1024).decode())
