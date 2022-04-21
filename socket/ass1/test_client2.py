# import socket
# import threading
# import queue
# import random
# import os

# IP_address = "192.168.1.5"
# FORMAT='utf-8'

# def RecieveData(obj):
#     while True:
#         try:
#             data, addr=obj.recvfrom(2048)
#             print(data.decode(FORMAT))
#         except:
#             pass

# def RunClient(IP):
#     host = "127.0.0.1"
#     port = random.randint(49152, 65535)
#     print('Client IP->'+str(host)+' Port->'+str(port))
#     server=(str(IP), 2002)
#     s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind((host, port))

#     name=input("Enter your name:")
#     if name=='':
#         name = 'Guest'+str(random.randint(1000,9999))
#         print('Your name is:'+name)
#     s.sendto(name.encode(FORMAT), server)
#     threading.Thread(target=RecieveData, args=(s,)).start()
#     while True:
#         data=input()
#         if data=="qqq":
#             break
#         elif data=="":
#             continue
#         data = '['+IP+"-"+name+']' + ': '+ data
#         s.sendto(data.encode(FORMAT), server)
#     s.sendto(data.encode(FORMAT), server)
#     s.close()
#     os._exit(1)

# RunClient(IP_address)

import socket
import threading
import queue
import sys
import random
import os

def ReceiveData(sock):
    while True:
        try:
            data,addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass
        
def RunClient(serverIP):
    host = "127.0.0.4"
    port = random.randint(6000,10000)
    print('Client IP->'+str(host)+' Port->'+str(port))
    server = (str(serverIP),5000)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    name = input('Please write your name here: ')
    if name == '':
        name = 'Guest'+str(random.randint(1000,9999))
        print('Your name is:'+name)
    s.sendto(name.encode('utf-8'),server)
    threading.Thread(target=ReceiveData,args=(s,)).start()
    while True:
        data = input()
        if data == 'qqq':
            break
        elif data=='':
            continue
        data = '['+name+']' + '->'+ data
        s.sendto(data.encode('utf-8'),server)
    s.sendto(data.encode('utf-8'),server)
    s.close()
    os._exit(1)
    
RunClient("127.0.0.1")