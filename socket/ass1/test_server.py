import socket
import threading
import queue
import random

# get the ip address of the server host machine
host = socket.gethostbyname(socket.gethostname())
port = 2002 # port on which the server will run
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_DGRAM is for UDP
s.bind((host,port)) # binding the server
# have a set of active clients
clients = set()
recvPackets = queue.Queue()
FORMAT='utf-8'

# this function is to handle all the packets after receiving
#  them and store them in a queue called recvPackets
def hande_client(recvPackets):
    while True:
        data,addr = s.recvfrom(1024)
        recvPackets.put((data,addr))

# the main function which is called when the server is starting
def start():
    print('[RUNNING] Server IP address: '+str(host))
    # create threads for clients
    threading.Thread(target=hande_client,args=(recvPackets,)).start()
    while True:
        while not recvPackets.empty():
            # get packets from the queue
            data,addr = recvPackets.get()
            if addr not in clients:
                # add the client to the set of active clients
                clients.add(addr)
                continue
            clients.add(addr)
            data = data.decode(FORMAT)
            if data.endswith('QUIT'):
                # when the user enters a message ending with QUIT 
                # the client is removed from the active clients
                clients.remove(addr)
                continue
            print(data)
            for c in clients:
                # print to every active client who is not the sender of the message
                if c!=addr:
                    s.sendto(data.encode(FORMAT),c)
    s.close()
    
print('[STARTING] Server is starting...')
start()