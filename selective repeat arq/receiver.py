import socket
import random
import math

print("")
print("** NAME: SIDDHARTH MANDAL **")
print("** REG NO. 20BDS0157 **")
print("")
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="192.168.1.5"
FORMAT="utf-8"
PORT=2005

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

while True:
    count=0
    temp=[]
    while count<4:
        # receive the frames from the sender
        val=rec.recv(2048).decode(FORMAT)
        val=int(val)
        count+=1
        temp.append(ar[rn+count])
    x=random.randint(0, 3)
    # make any one frame corrupted to simulate the not frame lost scenario
    temp[x]=-1
    for i in range(4):
        temp[i]=str(temp[i])
    print(temp)
    count=0

    while count<4:
        # send the acknowledgment to the sender
        print("Sending acknowledgment for ", str(rn+count))
        rec.send(temp[count].encode(FORMAT))
        count+=1
    val=rec.recv(2048).decode(FORMAT)
    val=int(val)
    print(str(val), "received again")
    rec.send(str(rn).encode(FORMAT))
    # move the frame
    rn+=4