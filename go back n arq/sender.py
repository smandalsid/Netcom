# SENDER SIDE

import socket
import math
import time

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
PORT=2002

server.bind((SERVER, PORT))
server.listen(1)

def handle_window(conn, addr):
    m=int(input("Enter value of m: "))
    size=int(input("Enter number of packets to send: "))
    ar=[]
    ssize=int(input("Enter size of window(greater than 0, less than "+str(math.pow(2,m)-1)+"): "))
    
    x=0
    for i in range(size):
        if x==(math.pow(2,m)):
            ar.append(0)
            x=1
        else:
            ar.append(x)
            x+=1
    print(ar)
    conn.send(str(m).encode(FORMAT))
    conn.send(str(size).encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    print("")
    sn=sf=0
    while((sf+ssize-1)!=(size)):
        while(sf!=size):
            # flag=1
            print("")
            print("Sending frame: "+str(ar[sn])+" sf: "+str(sf)+" sn: "+str(sn))
            time.sleep(1)
            conn.send(str(ar[sn]).encode(FORMAT))
            sn+=1
            ack=conn.recv(2048).decode(FORMAT)
            ack=int(ack)
            if(ar[sn]==ack):
                print("Acknowledgment for "+str(ar[sn-1])+" received")
                sf=sn
                flag=1
                print("new sf "+str(sf)+" new sn "+str(sf))
            else:
                print("Incorrect acknowledgment received...")
                if sn>=sf+ssize:
                    print("\nSending packets of the window again...\n")
                    sn=sf
            


def start():
    print("")
    print("** NAME: SIDDHARTH MANDAL **")
    print("** REG. NO. 20BDS0157 **")
    print("")
    print("[STARTING] Server is starting...")
    print("[LISTENING] Listening for a connection... ")
    conn, addr = server.accept()
    print("[REQUEST] Connecting...")
    print("[CONNECTED] IP address of receiver: "+str(addr[0])+" at PORT: "+str(addr[1]))
    handle_window(conn, addr)
    

start()
conn.close()
server.close()