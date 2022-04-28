# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# PORT=2002

# server.bind((SERVER, PORT))

# while True:
#     pair=server.recvfrom(2048)
#     msg=format(pair[0])
#     address=format(pair[1])
#     print(msg)
#     print(address)

# import math
# import socket
# import time
# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# PORT=2002
# FORMAT="utf-8"

# server.bind((SERVER, PORT))
# print("SERVER running at: "+SERVER)
# server.listen(1)
# conn, addr=server.accept()
# print("IP of client: "+str(addr[0])+" PORT: "+str(addr[1]))


# n=int(input("Enter number of packets: "))
# conn.send(str(n).encode(FORMAT))
# m=int(input("Enter value of m: "))
# conn.send(str(m).encode(FORMAT))
# ssize=int(input("Enter length of window: "))
# conn.send(str(ssize).encode(FORMAT))


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

# sn=sf=0

# while sn!=len(ar):
#     for i in range(sf, sf+ssize):
#         print("Sent frame: "+str(ar[sn]))
#         conn.send(str(ar[sn]).encode(FORMAT))
#         time.sleep(1)
#         sn+=1
#     resends=[]
#     flag=0
#     for i in range(sf, ssize+sf):
#         ack=conn.recv(2048).decode(FORMAT)
#         print("Ack received: "+ack)
#         if int(ack)==ar[sf+1]:
#             if flag==0:
#                 sf+=1
#                 print("sf: "+str(sf)+" sn: "+str(sn))
#         else:
#             flag=1
#             print("Incoorect ack received for frame: "+str(ar[sf]))
            
#     if flag==1:
#         print("Sending frame again: "+str(ar[sf]))
#         conn.send(str(ar[sf]).encode(FORMAT))
#         conn.recv(2048).decode(FORMAT)
#         print("Ack received")
#         sf=sn
#         print("sf: "+str(sf)+" sn: "+str(sn))

# import socket
# import math

# # data=input("Enter dataword: ")
# data="01001000111"
# l=[]
# temp=data[::-1]

# i=0
# j=0
# while len(temp)>0:
#     if (i+1)==math.pow(2, j):
#         l.append('')
#         j+=1
#         i+=1
#     else:
#         l.append(temp[0])
#         i+=1
#         temp=temp[1:]

# j=0
# print(l)
# for i in range(len(l)):
#     if (i+1)==math.pow(2, j):
#         count=0
#         for k in range(i+1, len(l)):
#             if int(i+1)&int(k+1)==int(i+1):
#                 if l[k]=='1':
#                     count+=1
#         if count%2==0:
#             l[i]='1'
#         else:
#             l[i]='0'
#         j+=1

# print(l[::-1])

# dataword="1010011110"
# divisor="10111"

# def xor(a, b):
#     temp=""
#     flag=0
#     for i in range(len(a)):
#         if int(a[i])^int(b[i]):
#             temp+='1'
#             flag=1
#         elif flag==1:
#             temp+='0'
#     return temp

# def division(dividend, divisor):
#     while len(dividend)>=len(divisor):
#         dividend=xor(dividend[:len(divisor)], divisor)+dividend[len(divisor):]
#     return dividend

# temp=dataword
# for i in range(len(divisor)-1):
#     temp+='0'

# remainder=division(temp, divisor)

# print(remainder)

# temp=dataword+remainder
# print(temp)

import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
PORT=2002
FORMAT='utf-8'
server.bind((SERVER, PORT))
print("SERVER running at: "+SERVER)
server.listen(1)
conn, addr=server.accept()
print("Client IP: "+str(addr[0])+" PORT: "+str(addr[1]))
