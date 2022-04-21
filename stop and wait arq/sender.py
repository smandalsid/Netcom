
# SENDER SIDE

import socket
import math
import time

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
PORT=2003

# bind the server
server.bind((SERVER, PORT))
# listen for 1 connection
server.listen(1)


# handle the sending of frames and receiving of ackowledgments
def handle_window(conn, addr):
    m=int(input("Enter value of m: "))
    size=int(input("Enter number of packets to send: "))
    ar=[]
    ssize=int(input("Enter size of window(greater than 0, less than "+str(m-1)+"): "))
    
    x=0
    # create an array for the frames
    for i in range(size):
        if x==0:
            ar.append(0)
            x=1
        else:
            ar.append(x)
            x=0
    # send m value
    conn.send(str(m).encode(FORMAT))
    conn.send(str(size).encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    print("")
    sn=0
    # while((sf+ssize-1)!=(size)):
    while(sn!=size):
        # flag=1
        print("")
        print("Sending frame: "+str(ar[sn])+" sn: "+str(sn))
        time.sleep(1)
        conn.send(str(ar[sn]).encode(FORMAT))
        sn+=1
        ack=conn.recv(2048).decode(FORMAT)
        ack=int(ack)
        if(ar[sn]==ack):
            print("Acknowledgment for "+str(ar[sn-1])+" received")
            # sf=sn
            flag=1
            print("new sn "+str(ar[sn]))
        else:
            print("Incorrect acknowledgment received...")
            


def start():
    print("")
    print("***** NAME: SIDDHARTH MANDAL *****")
    print("***** REG. NO. 20BDS0157 *****")
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

