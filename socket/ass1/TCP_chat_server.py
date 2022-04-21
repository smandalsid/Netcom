# Python program to implement server side of chat room.
import socket
import select
from _thread import *

# AF_INET is to specify the type of addresses that our socket can communicate in, in this case we are using Internet Protocol V4 addresses
# SOCK_STREAM indicates that it is a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the IP address of the server machine
SERVER = socket.gethostbyname(socket.gethostname())

# for encoding and decoding our messages before sending and recieving
FORMAT="utf-8"

# the port on which our server will be listening or clients
PORT = int(2002)

# binds our server to the IP address and the PORT number
server.bind((SERVER, PORT))
server.listen(100)

# list to keep track of active clients
list_of_clients = []

# function to handle the clients and takes conn which is an object of the client and addr is its IP address
def handle_client(conn, addr):

	# welcome the client to the chatroom
	conn.send("Welcome to this chatroom!".encode(FORMAT))
    
	while True:
		try:
			# recieve message from the client
			message = conn.recv(2048).decode(FORMAT)
			if message:

				# print the message from the client on the server side
				print ("<" + addr[0] + "> " + message)

				# prepare the recieved message from the client to broadcast to the other clients
				broadcast_message = "<" + addr[0] + "> " + message
				# boradcast the message to all the other clients
				broadcast(broadcast_message, conn)
			else:
				# remove the client when the connection is broken
				remove(conn)
        
		except:
			continue

# function to transmit of one client to all other clients
# whose object is not same as the object of the client 
# who sent the message, it recieves the object of the client
# sending the message and the msg to broadcast
def broadcast(msg, conn):
	for client in list_of_clients:
		if client!=conn:
			try:
				client.send(msg.encode(FORMAT))
			except:
				client.close()

				remove(client)

# function to remove a client from active clients when a
# connection is broken
def remove(conn):
	if conn in list_of_clients:
		list_of_clients.remove(conn)


# function that will be called when the program starts
def start():
    while True:
		# print("[RUNNING] Address: "+server)

		# it is to accept new connections and get their
		# socket object conn and their IP address addr
        conn, addr = server.accept()

		# append the client to the list of active clients
        list_of_clients.append(conn)
        print (addr[0] + " connected")

		# every client is handled by a thread
		# as when a thread is waiting to take input the other thread can run
        start_new_thread(handle_client,(conn,addr))	
    conn.close()
    server.close()

# notify when the server starts
print("[STARTING] Server is starting...")
print("[RUNNING] Address: "+SERVER)
start()