import socket
import numpy as np
import math

port=2003
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, port))

# check if this position has to be checked while assigning value of redundant bit
def validate(i, j):
    i=bin(i)
    j=bin(j)
    i=i[2:]
    j=j[2:]

    maxs=len(j)
    while len(i)!=maxs:
        i='0'+i

    pos=i.index('1')
    if j[pos]=='1':
        return True
    else:
        return False
    
# generate the hamming code and send to the receiver
def handle_client(conn, addr):
    # take input
    dataword=input("Enter dataword: ")
    print("")
    print(conn.recv(2048).decode(FORMAT))
    # dataword="01001000111"
    l=len(dataword)
    rb=0
    while 2**rb<l:
        rb+=1
        l+=1

    # generate two lists which will have the generated hamming code and the index positions
    ar=np.full(l, -1)
    posar=np.arange(l, 0, -1)
    ar=list(ar)
    posar=list(posar)
    pos1=0
    pos2=rb-1

    #  add the bits of dataword to the hamming code keeping space for the redundant bits
    for i in range(l):
        if posar[i]!=2**pos2:
            ar[i]=int(dataword[pos1])
            pos1+=1
        else:
            pos2-=1


    # add the redundant bits according to ODD parity
    pos2=0
    for i in range(1, l+1):
        count=0

        if i==2**pos2:
            pos2+=1
            for j in range(i+1, l+1):
                if validate(i, j) and ar[posar.index(j)]==1:
                    count+=1
        
            if count%2==0:
                ar[posar.index(i)]=1
            else:
                ar[posar.index(i)]=0

    for i in range(len(ar)):
        ar[i]=str(ar[i])
    message=""     
    message=message.join(ar)
    
    #  send the generated hamming code
    print("Hamming code generated: ", message)
    
    conn.send(message.encode(FORMAT))
    print("Data sent\n")
    # print("ar: ", ar)
    # print("posar: ", posar)

def start():
    print("\n****** SIDDHARTH MANDAL ******")
    print("****** REG. NO. 20BDS0157 ******\n")
    # listening for a connection
    server.listen(1)
    print("[STARTING] Sender is ready...")
    print("[LISTENING] Listening for a connection... ")
    # accept a connection
    conn, addr=server.accept()
    print("[REQUEST] Connecting...")
    print("[CONNECTED] IP address of receiver: "+str(addr[0])+" at PORT: "+str(addr[1]))
    handle_client(conn, addr)

    conn.close()
    server.close()

start()