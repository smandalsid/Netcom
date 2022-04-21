import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip="172.16.146.109"
PORT=2005

server.connect((ip, PORT))
FORMAT="utf-8"

while True:
    print(server.recv(2048).decode(FORMAT))
    msg=input()
    server.send(msg.encode(FORMAT))
    print(server.recv(2048).decode(FORMAT))