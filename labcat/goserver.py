import socket
import math

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP=socket.gethostbyname(socket.gethostname())
PORT=2003
FORMAT="utf-8"

server.bind((SERVER_IP, PORT))
server.listen(1)

def handle_window(conn, addr):
    m=int(input("Enter value of m:"))
    size=int(input("Enter number of packets"))
    ar=[]
    ssize=int(input("Enter window size"))

    x=0
    for i in range(size):
        if x==math.pow(2,m):
            ar.append(0)
            x=1
        else:
            ar.append(x)
            x+=1
    print(ar)

    conn.send(str(m).encode(FORMAT))
    conn.send(str(size).encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    conn.send(str(ssize).encode(FORMAT))



    sn=sf=0
    while (sf+ssize)!=(size):
        for i in range(sf, sf+ssize):
            print("sending frame:"+str(ar[i]))
            conn.send(str(ar[sn]).encode(FORMAT))
            print("SN:"+str(sn))
            sn+=1
        acks=[]
        correct=0
        for i in range(sf, sf+ssize):
            acks.append(conn.recv(2048).decode(FORMAT))
        for i in range(sf, sf+ssize):
            if int(acks[i])==ar[i+1]:
                print("ACK for "+str(ar[i])+" recieved")
                correct+=1
                
            else:
                print("Sending packets of window again")
                break
        if correct==ssize:
            sf+=ssize
            print("SF:"+sf)
        
        
    conn.send()

def start():
    print("SIDDHARTH MANDAL")
    print("Server running at:"+SERVER_IP)
    print("waiting for connections")
    conn, addr=server.accept()
    print("Connected, IP address:"+str(addr[0])+" From port"+str(addr[1]))
    handle_window(conn, addr)

start()