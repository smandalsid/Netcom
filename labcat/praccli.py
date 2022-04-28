# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SERVER="172.16.145.190"
# PORT=2002


# while True:
#     msg=input()
#     msgbytes=str.encode(msg)
#     server.sendto(msgbytes, (SERVER, PORT))

# import math
# import socket
# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER="172.16.145.190"
# PORT=2002
# server.connect((SERVER, PORT))
# FORMAT="utf-8"

# n=int(server.recv(2048).decode(FORMAT))
# print(n)
# m=int(server.recv(2048).decode(FORMAT))
# print(m)
# ssize=int(server.recv(2048).decode(FORMAT))
# print(ssize)

# ar=[]
# i=0
# while len(ar)!=n:
#     if i==math.pow(2,m):
#         ar.append(0)
#         i=1
#     else:
#         ar.append(i)
#         i+=1
# print(ar)

# rn=0

# while(rn!=len(ar)):
#     for i in range(rn, rn+ssize):
#         print("Received frame: ", end='')
#         val=server.recv(2048).decode(FORMAT)
#         print(val)
#     flag=0
#     temp=rn
#     for i in range(ssize):
#         ack=input("Enter ack to send: ")
#         if int(ack)!=ar[rn+1]:
#             flag=1
#         elif int(ack)==ar[rn+1] and flag==0:
#             rn+=1
#             print("rn: "+str(rn))
#         # elif 
#         server.send(ack.encode(FORMAT))
#     if flag==1:
#         val=server.recv(2048).decode(FORMAT)
#         print("Received frame again: "+val)
#         server.send(str(ar[rn+1]).encode(FORMAT))
#         print("Ack sent")
#         if int(ack)==ar[rn+1]:
#             rn=temp+ssize-1

import socket
import math