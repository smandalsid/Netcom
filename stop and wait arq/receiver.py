import socket
import random
import math

print("")
print("***** NAME: SIDDHARTH MANDAL *****")
print("***** REG NO. 20BDS0157 *****")
print("")
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="192.168.1.5"
FORMAT="utf-8"
PORT=2003

print("[CONNECTING] Conneting with the sender...")
# connect with the sender
rec.connect((SENDER, PORT))
print("Connected...")

m=rec.recv(2048).decode(FORMAT)
size=rec.recv(2048).decode(FORMAT)
print(size)
m=int(m)
size=int(size)
ar=[]
x=0
# create an array for the frames
for i in range(size):
    if x==0:
        ar.append(0)
        x=1
    else:
        ar.append(x)
        x=0
print(ar)
inp=""
rn=1
rec.send("RECEIVER: READY to receive...".encode(FORMAT))
print("rn: "+str(rn))
while True:
    # receive from the sender
    val=rec.recv(2048).decode(FORMAT)
    val=int(val)
    r=random.randint(0,1) # to show how the code works when we correct and incorrect ack are sent
    if(r==0):
        if(rn!=len(ar)):
            if(ar[rn]==val):
                rn+=1
        else:
            break
        rec.send(str(ar[rn]).encode(FORMAT))
    else:
        rec.send(str(-1).encode(FORMAT))
    print("rn: "+str(ar[rn]))

rec.close()