# import math
# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER="172.16.145.190"
# PORT=2002
# FORMAT="utf-8"
# server.connect((SERVER, PORT))

# msg=server.recv(2048).decode(FORMAT)
# print(msg)
# # msg="010010010110110"
# l=[]
# for i in msg:
#     l.append(i)

# temp=l[::-1]
# k=0
# ans=""
# for i in range(len(temp)):
#     count=0
#     if (i+1)==math.pow(2, k):
#         for j in range(i, len(temp)):
#             if (i+1)&(j+1)==i+1:
#                 if temp[j]=='1':
#                     count+=1
#         k+=1
#         if count%2!=0:
#             ans+='0'
#         else:
#             ans+='1'

# k=0
# bit=0
# print("Ans: "+ans)
# for i in ans:
#     bit+=(int(ans[k])*math.pow(2,k))
#     k+=1

# print(int(bit))

# # server.send(str(int(bit)).encode(FORMAT))

# server.close()

# CRC CRC CRC CRC

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER="172.16.145.190"
# PORT=2002
# server.connect((SERVER, PORT))
# FORMAT="utf-8"

# codeword=server.recv(2048).decode(FORMAT)
# print("Received codeword: "+codeword)
# divisor=server.recv(2048).decode(FORMAT)
# print("Divisor: "+divisor)

# codeword="10100011101010"
# divisor="10111"

# def xor(a, b):
#     temp=""
#     flag=0
#     for i in range(len(a)):
#         if (int(a[i])^int(b[i]))==1:
#             temp+='1'
#             flag=1
#         elif flag==1:
#             temp+='0'
#     print(temp, end=" ")
#     return temp

# def division(dividend, divisor):
#     while len(dividend)>=len(divisor):
#         dividend=xor(dividend[:len(divisor)], divisor)+dividend[len(divisor):]
#         print(dividend)
#     return dividend

# remainder=division(codeword, divisor)
# while(len(remainder)!=4):
#     remainder='0'+remainder
# print("remainder: "+remainder)



# for i in range(len(remainder)):
#     if remainder[i]!='0':
#         print("Data word rejected")
#         exit(0)

# print("data word accepted")
# server.close()

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SERVER=("172.16.145.190", 2002)

# while True:
#     # msg="This is from the client"
#     msg=input("Messgae: ")
#     msgbytes=str.encode(msg)
#     server.sendto(msgbytes, SERVER)
#     msg=server.recvfrom(2048)
#     print("Message from server: "+str(msg[0]))

# STOP AND WAIT

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER="172.16.145.190"

# FORMAT="utf-8"
# PORT=2002

# server.connect((SERVER, PORT))

# n=server.recv(2048).decode(FORMAT)
# print("Numeber of packets: "+n)
# n=int(n)
# ar=[]
# i=0
# while len(ar)!=n:
#     if i==0:
#         ar.append(0)
#         i=1
#     else:
#         ar.append(1)
#         i=0
# print(ar)
# rn=0

# while(rn!=len(ar)-1):
#     frame=server.recv(2048).decode(FORMAT)
#     print("Received frame: "+frame)
#     userack=input("Enter Ack to send: ")
#     if userack==str(ar[rn]):
#         rn+=1
#     server.send(userack.encode(FORMAT))
#     print("Sent ack: "+userack)
#     print("rn: "+str(rn))
#     frame=""
#     # if frame==str(ar[rn]):
#     #     rn+=1
#     # server.send(str(ar[rn]).encode(FORMAT))
#     # print("Sent ack: "+ar[rn])

# GO BACK N ARQ

# import socket
# import math

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER="172.16.145.190"

# FORMAT="utf-8"
# PORT=2001

# server.connect((SERVER, PORT))

# n=server.recv(2048).decode(FORMAT)
# m=server.recv(2048).decode(FORMAT)
# ar=[]

# n=int(n)
# m=int(m)
# i=0
# while len(ar)!=n:
#     if i<math.pow(2,m):
#         ar.append(i)
#         i+=1
#     else:
#         ar.append(0)
#         i=1
# print(ar)
# rn=0
# l=[]
# while True:
#     l=[]
#     for i in range(3):
#         l.append(server.recv(2048).decode(FORMAT))
#         print("Received frame: "+l[-1])
    
#     for i in range(3):
#         ack=input()
#         if str(ar[rn+1])==ack:
#             rn+=1
#             print("rn: "+str(rn))
#             server.send(str(ack).encode(FORMAT))
#         else:
#             print("Sending incorrect ack")
#             server.send(str(ack).encode(FORMAT))
#             break
    
#         print("Sending ack: "+ack)

import socket

