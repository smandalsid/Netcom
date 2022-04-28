import socket
import threading
import queue
import random
import os

# IP of the client
IP = "127.0.0.1"
# IP of the server
serverIP="172.16.145.190"
# generate a random port number for the client
port = random.randint(6000,10000)
print('Client IP: '+str(IP)+' Port: '+str(port))
server = (str(serverIP),2002)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((IP,port))

# recieve messages from the server
def fromserver(sock):
    while True:
        try:
            data,addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass
        
# main function called by a client
def startclient(serverIP):
    # takes the name of the client
    name = input('Please enter your name: ')
    # assigns a guest name in case name not entered
    if name == '':
        name = 'Guest'+str(random.randint(1000,9999))
        print('Your name is:'+name)
    s.sendto(name.encode('utf-8'),server)
    # thread to get messages from the server when the server sends messages
    threading.Thread(target=fromserver,args=(s,)).start()
    while True:
        data = input()
        if data.endswith("QUIT"):
            break
        elif data=='':
            continue
        data = '['+serverIP+'-'+name+']' + '->'+ data
        s.sendto(data.encode('utf-8'),server)
    s.sendto(data.encode('utf-8'),server)
    s.close()
    os._exit(1)
    
startclient(serverIP)