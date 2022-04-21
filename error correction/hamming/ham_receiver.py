import socket
import numpy

print("")
print("** NAME: SIDDHARTH MANDAL **")
print("** REG NO. 20BDS0157 **")
print("")
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="192.168.1.5"
FORMAT="utf-8"
PORT=2002

print("[CONNECTING] Conneting with the sender...")
# connect with the sender
rec.connect((SENDER, PORT))
print("Connected...")

# receive the hamming code from the sender
rec.send("RECEIVER: READY to receive...".encode(FORMAT))
msg=rec.recv(2048).decode(FORMAT)
# to simulate a condition when there is error in transmission
msg="010000010110110"
print("\nData received: ", msg)

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

ar=[]
for i in msg:
    ar.append(int(i))
l=len(ar)
posar=[]

for i in range(l, 0, -1):
    posar.append(i)

ans=[]
pos=0
for i in range(1, l+1):
    count=0
    if i==2**pos:
        pos+=1
        for j in range(i, l+1):
            if validate(i, j) and ar[posar.index(j)]==1:
                count+=1

        # if the number of 1's is odd then append 0 to a list, else 1
        if count%2!=0:
            ans.append(0)
        else:
            ans.append(1)

bit=0
pos=0
flag=0
# converting the 
for i in ans:
    if i==1:
        flag=1
    bit+=i*(2**pos)
    pos+=1
ans.reverse()

if flag==1:
    print("\nError detected in bit: ", bit)
else:
    print("\nWord accepted")