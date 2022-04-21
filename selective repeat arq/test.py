import socket
import math
import time



server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
PORT=1234

server.bind((SERVER, PORT))
server.listen(1)


def func(conn, addr):
    # get the imputs from the user
    a=int(input())
    b=int(input())
    c=[]
    d=int(input())
    
    x=0
    for i in range(b):
        if x==(math.pow(2,a)):
            c.append(0)
            x=1
        else:
            c.append(x)
            x+=1
    conn.send(str(a).encode(FORMAT))
    conn.send(str(b).encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    sn=sf=0

    while((sf+d-1)!=b):
        while(sn!=sf+d):
            conn.send(str(c[sn]).encode(FORMAT))
            sn+=1
        rar=[]
        temp=0
        
        while(temp<4):
            rar.append(int(conn.recv(2048).decode(FORMAT)))
            if rar[-1]!=-1:
                print("ACK ", rar[-1], " received")
            else:
                nakpos=sf+temp
            temp+=1
        
        conn.send(str(c[nakpos]).encode(FORMAT))
        ack=conn.recv(2048).decode(FORMAT)
        sf+=4


def start():
    print("")
    print("** NAME: SIDDHARTH MANDAL **")
    print("** REG. NO. 20BDS0157 **")
    print("")
    conn, addr = server.accept()
    func(conn, addr)
    

start()