
# HAMMING HAMMING HAMMING 

# import math
# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# print("IP address of server: "+SERVER)
# FORMAT='utf-8'
# PORT=2002
# server.bind((SERVER, PORT))
# server.listen(1)
# conn, addr=server.accept()
# print("IP of connected client: "+str(addr[0])+" port: "+str(addr[1]))

# # data=input("Enter dataword\n")
# # data="01001000111"
# data="01001000111"
# temp=data[::-1]

# l=[]
# i=1
# pos=0
# j=0
# while pos!=len(temp):
#     if i==math.pow(2, j):
#         l.append('')
#         i+=1
#         j+=1
#     else:
#         l.append(temp[pos])
#         pos+=1
#         i+=1
# l=l[::-1]
# print(l)

# print("Let us consider even parity")
# temp=l[::-1]
# k=0
# for i in range(len(temp)-1):
#     count=0
#     if (i+1)==math.pow(2,k):
#         for j in range(i+1,len(temp)):
#             # print("HI")
#             if (int(i+1))&(int(j+1))==int(i+1):
#                 if temp[j]=='1':
#                     count+=1
#         if count%2!=0:
#             temp[i]='0'
#         else:
#             temp[i]='1'
#         k+=1


# print(temp[::-1])
# msg=""

# for i in range(len(temp)-1, -1, -1):
#     msg+=temp[i]

# print(msg)


# print("Sending codeword to client")
# temp="010000010110110"
# conn.send(temp.encode(FORMAT))

# conn.close()
# server.close()


# CRC CRC CRC

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# PORT=2002
# FORMAT="utf-8"
# server.bind((SERVER, PORT))
# print("SERVER running at: "+ SERVER)
# server.listen(1)
# conn, addr=server.accept()
# print("Client connected at: "+str(addr[0])+" port: "+str(addr[1]))

# def xor(a, b):
#     temp=""
#     flag=0
#     for i in range(len(a)):
#         if (int(a[i])^int(b[i])):
#             temp+='1'
#             flag=1
#         elif flag==1:
#             temp+='0'
#     # print(temp, end=" ")
#     return temp

# def divide(dividend, divisor):
#     while len(dividend)>=len(divisor):
#         dividend=xor(dividend[:len(divisor)], divisor)+dividend[len(divisor):]
#         # print(dividend)
#     return dividend

# # data=input("Enter dataword:\n")
# dataword="1010011110"
# # divisor="10111"
# # dataword="10100011101010"
# divisor="10111"

# dividend=dataword
# for i in range(len(divisor)-1):
#     dividend+='0'

# # dividend="10100011101010"
# remainder=divide(dividend, divisor)
# print("Remainder: "+remainder)
# msg=dataword
# while len(remainder)!=len(divisor)-1:
#     remainder='0'+remainder
# msg=msg+remainder

# msg="10100111101010"
# # divisor="10111"
# conn.send(msg.encode(FORMAT))
# print("Codeword being sent to user: "+msg)
# conn.send(divisor.encode(FORMAT))
# print("Sending divisor")

# conn.close()
# server.close()

# UDP UDP UDP

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# print("IP of the server: "+SERVER)
# PORT=2002

# server.bind((SERVER, PORT))

# while True:
#     pair=server.recvfrom(2048)
#     msg=format(pair[0])
#     address=pair[1]
#     print("Message: "+msg)
#     print("IP of the client: "+format(address))
#     msg="Your message was received"
#     msgbytes=str.encode(msg)
#     server.sendto(msgbytes, address)

# STOP AND WAIT

# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# FORMAT="utf-8"
# PORT=2002

# server.bind((SERVER, PORT))
# print("SERVER running at: "+SERVER)

# server.listen(1)
# conn, addr=server.accept()
# print("IP of client: "+str(addr[0])+" port: "+str(addr[1]))

# n=int(input("Enter number of frames to send: "))
# i=0
# ar=[]
# while len(ar)<n:
#     if i==0:
#         ar.append(i)
#         i=1
#     else:
#         ar.append(i)
#         i=0

# print(ar)
# conn.send(str(n).encode(FORMAT))
# w=0
# sn=0
# flag=0
# while sn!=len(ar):
#     conn.send(str(ar[sn]).encode(FORMAT))
#     if flag==0:
#         print("Sent frame: "+str(ar[sn]))
#     else:
#         print("Sent frame: "+str(ar[sn])+" again")
#         flag=0
#     ack=conn.recv(2048).decode(FORMAT)
#     print("Received Ack: "+ack)
    
#     if(sn!=len(ar)-1):
#         if(ar[sn+1]==int(ack)):
#             sn+=1
#             print("sn: "+str(sn))
#         else:
#             # conn.send(str(ar[sn]).encode(FORMAT))
#             # print("Send frame: "+str(ar[sn])+" again.")
#             flag=1

# GO BACK N ARQ

# import math
# import socket

# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER=socket.gethostbyname(socket.gethostname())
# PORT=2001
# FORMAT="utf-8"

# server.bind((SERVER, PORT))
# print("SERVER running at: "+SERVER)
# server.listen(1)
# conn, addr=server.accept()
# print("CONNECTED, IP of client: "+str(addr[0])+"PORT: "+str(addr[1]))

# n=int(input("Enter number of packets to send: "))
# conn.send(str(n).encode(FORMAT))
# m=int(input("Enter value of m: "))
# conn.send(str(m).encode(FORMAT))
# # ssize=int(math.pow(2, m)-1)
# ssize=int(input("Enter size of window: "))
# ar=[]
# i=0
# while len(ar)!=n:
#     if i<math.pow(2,m):
#         ar.append(i)
#         i+=1
#     else:
#         ar.append(0)
#         i=1
# print(ar)

# sf=sn=0

# resend=0
# while sn!=len(ar):
#     for i in range(sf, sf+ssize):
#         if resend==1:
#             print("Sending frame again: "+str(ar[sn]))
#             conn.send(str(ar[sn]).encode(FORMAT))
#             sn+=1
#             print("sf: "+str(sf)+" sn: "+str(sn))
#         else:
#             print("Sending frame: "+str(ar[sn]))
#             conn.send(str(ar[sn]).encode(FORMAT))
#             sn+=1
#             print("sf: "+str(sf)+" sn: "+str(sn))
#     temp=sf
#     resend=0
#     for i in range(temp, temp+ssize):
#         ack=conn.recv(2048).decode(FORMAT)
#         # ack=input()
#         print("ACK received: "+ack)
#         if ack==str(ar[sf+1]):
#             sf+=1
#             print("sf: "+str(sf)+" sn: "+str(sn))
#         else:
#             print("Incorrect ACK received")
#             resend=1
#             sn=sf
#             break


# IP IP IP

# import math

# ip="172.16.0.0/25"

# iplist=ip.split('.')
# temp=iplist[-1].split('/')
# iplist[-1]=temp[0]
# iplist.append(temp[1])

# for i in range(len(iplist)):
#     iplist[i]=int(iplist[i])

# ipbinlist=[]
# for i in range(len(iplist)-1):
#     ipbinlist.append(bin(iplist[i]))
#     ipbinlist[-1]=ipbinlist[-1][2:]
#     while len(ipbinlist[-1])!=8:
#         ipbinlist[-1]='0'+ipbinlist[-1]

# defaultclass=""
# if ipbinlist[0][0]=='0':
#     defaultclass='a'
# elif ipbinlist[0][:2]=='10':
#     defaultclass='b'
# elif ipbinlist[0][:3]=='110':
#     defaultclass='c'

# if defaultclass=='a':
#     defaultmask=8
# elif defaultclass=='b':
#     defaultmask=16
# else:
#     defaultmask=24

# subnetmask=['', '', '', '']
# count=iplist[-1]

# for i in range(4):
#     for j in range(8):
#         if count>0:
#             subnetmask[i]+='1'
#             count-=1
#         else:
#             subnetmask[i]+='0'

# subnetaddress=['', '', '', '']
# for i in range(4):
#     for j in range(8):
#         subnetaddress[i]+=str(int(ipbinlist[i][j])&int(subnetmask[i][j]))
# fsubnetaddress=''
# for i in range(4):
#     fsubnetaddress=fsubnetaddress+str(int(subnetaddress[i], 2))+'.'

# fsubnetaddress=fsubnetaddress[:len(fsubnetaddress)-1]

# broadcastaddress=['', '', '' ,'']
# count=iplist[-1]
# for i in range(4):
#     for j in range(8):
#         if count>0:
#             broadcastaddress[i]+=ipbinlist[i][j]
#             count-=1
#         else:
#             broadcastaddress[i]+='1'

# fbroadcastaddress=''
# for i in range(4):
#     fbroadcastaddress=fbroadcastaddress+str(int(broadcastaddress[i], 2))+'.'
# fbroadcastaddress=fbroadcastaddress[:len(fbroadcastaddress)-1]

# print("Number of subnets: "+str(2**(iplist[-1]-defaultmask)))
# print("Number of hosts per subnet: "+str(2**(32-iplist[-1])-2))
# print("Subnet address: ", fsubnetaddress)
# print("Broadcast address: ", fbroadcastaddress)

# subnetlist=fsubnetaddress.split('.')
# subnetlist[-1]=str(int(subnetlist[-1])+1)
# firsthostid="".join(x+'.' for x in subnetlist)
# firsthostid=firsthostid[:len(firsthostid)-1]
# subnetlist[-1]=str(int(subnetlist[-1])+2**(32-iplist[-1])-2-1)
# lasthostid="".join(x+"." for x in subnetlist)
# lasthostid=lasthostid[:len(lasthostid)-1]


# print("First host id in first subnet block: ", firsthostid)
# print("Last host id in first subnet block: ", lasthostid)


import socket
import math

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
PORT=2002
print("IP of server: "+SERVER)
server.bind((SERVER, PORT))
server.listen(1)
conn, addr=server.accept()

print("IP of client: "+str(addr[0])+" port: "+str(addr[1]))

n=int(input("Enter number of packets to send: "))
m=int(input("Enter value of m: "))
ssize=int(input("Enter window size: "))

ar=[]
i=0
while len(ar)!=n:
    if i==math.pow(2,m):
        ar.append(0)
        i=1
    else:
        ar.append(i)
        i+=1
print(ar)

sn=sf=0
while sn!=len(ar):
    for i in range(4):
        print("Sending frame: "+str(ar[i]))
        sn+=1
    acks=[]
    for i in range(4):
        # ack.append(conn.recv(2048).decode(FORMAT))
        print("Ack received: "+ack[-1])
    resends=[]
    flag=0
    for i in range(4):
        if int(ack[i])==ar[sf+1]:
            if flag==0:
                sf+=1
        else:
            flag=1
            resends.append(sn)
    conn.send(str(len(resends)).encode(FORMAT))
    for i in range(len(resends)):
        conn.send(str(resends[i]).encode(FORMAT))
    acks2=[]
    for i in range(len(resends)):
        acks2.append(conn.recv(2048).decode(FORMAT))
        if ack2[-1]==str(ar[sf+1]):
            sf+=1
    
