# SENDER SIDE

import socket
import math
import time


# define the socket, port, server ip address and the format
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
PORT=2005

server.bind((SERVER, PORT))
server.listen(1)


# to send meessages to the receiver
def handle_window(conn, addr):
    # get the imputs from the user
    m=int(input("Enter value of m: "))
    size=int(input("Enter number of packets to send: "))
    ar=[]
    ssize=int(input("Enter size of window(greater than 0, less than "+str(math.pow(2,m)-1)+"): "))
    
    x=0
    # create the array of frames
    for i in range(size):
        if x==(math.pow(2,m)):
            ar.append(0)
            x=1
        else:
            ar.append(x)
            x+=1
    print(ar)
    # send m and the sizeof the array
    conn.send(str(m).encode(FORMAT))
    conn.send(str(size).encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    print("")
    sn=sf=0

    while((sf+ssize-1)!=size):
        print("Sending frames:")
        # send all the frames in the window
        while(sn!=sf+ssize):
            conn.send(str(ar[sn]).encode(FORMAT))
            sn+=1
            print("sn: ", str(sn))
        rar=[]
        temp=0
        
        # receives the ACKs and the NAKs
        while(temp<4):
            rar.append(int(conn.recv(2048).decode(FORMAT)))
            if rar[-1]!=-1:
                print("ACK ", rar[-1], " received")
            else:
                print("NAK ", ar[sf+temp], " received")
                nakpos=sf+temp
            temp+=1
        
        # send the lost frame again
        print("Sending lost frame again: ", str(ar[nakpos]))
        conn.send(str(ar[nakpos]).encode(FORMAT))
        ack=conn.recv(2048).decode(FORMAT)
        print("Acknowledgment for frame sent again received")
        sf+=4
        print("sf: "+str(sf)+" sn: "+str(sn))


def start():
    print("")
    print("** NAME: SIDDHARTH MANDAL **")
    print("** REG. NO. 20BDS0157 **")
    print("")
    print("[STARTING] Server is starting...")
    print("[LISTENING] Listening for a connection... ")
    # accept a connection
    conn, addr = server.accept()
    print("[REQUEST] Connecting...")
    print("[CONNECTED] IP address of receiver: "+str(addr[0])+" at PORT: "+str(addr[1]))
    handle_window(conn, addr)
    

start()
conn.close()
server.close()