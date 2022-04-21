import socket
import random
import math

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP="172.16.146.109"
PORT=2003
FORMAT="utf-8"
server.connect((IP, PORT))

m=int(server.recv(2048).decode(FORMAT))
size=int(server.recv(2048).decode(FORMAT))
server.send("Ready to recv".encode(FORMAT))
ssize=int(server.recv(2048).decode(FORMAT))

print("m:"+str(m))
print("size:"+str(size))
print("ssize:"+str(ssize))

ar=[]
x=0
for i in range(size):
    if x==math.pow(2,m):
        ar.append(0)
        x=1
    else:
        ar.append(x)
        x+=1
rn=0
print(ar)
while True:
    acks=[]
    for i in range(ssize):
        val=server.recv(2048).decode(FORMAT)
        if ar[rn]==int(val):
            rn+=1
            acks.append(str(ar[rn]))
    choices=[0,1]
    y=random.choice(choices)
    if y==0:
        for i in range(ssize):
            server.send(acks[i].encode(FORMAT))
    else:
        x=random.choice(acks)
        for i in range(ssize):
            if acks[i]!=x:
                server.send(acks[i].encode(FORMAT))
            else:
                server.send(acks[i].encode(FORMAT))
        