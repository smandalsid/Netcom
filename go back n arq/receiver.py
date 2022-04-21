import socket
import random
import math

print("")
print("** NAME: SIDDHARTH MANDAL **")
print("** REG NO. 20BDS0157 **")
print("")
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="172.16.146.109"
FORMAT="utf-8"
PORT=2002

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
    if x==(math.pow(2,m)):
        ar.append(0)
        x=1
    else:
        ar.append(x)
        x+=1
print(ar)
inp=""
rn=0
rec.send("RECEIVER: READY to receive...".encode(FORMAT))
print("rn: "+str(rn))
count=2
count2=3
while True:
    # receive from the sender
    val=rec.recv(2048).decode(FORMAT)
    val=int(val)
    
    if(count>0):
        count-=1
        if(rn!=len(ar)):
            if(ar[rn]==val):
                rn+=1
        else:
            break
        rec.send(str(ar[rn]).encode(FORMAT))
    else:
        rec.send(str(-1).encode(FORMAT))
        if count2==0:
            count=2
            count2=3
        else:
            count2-=1
    print("rn: "+str(ar[rn]))

rec.close()