# Python program to implement client side of chat room.
import socket
import select
import sys

# AF_INET is to specify the type of addresses that our socket can communicate in, in this case we are using Internet Protocol V4 addresses
# SOCK_STREAM indicates that it is a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "172.16.146.109"
PORT = 2002

# connect to the server using the ip address and the port
server.connect((IP_address, PORT))
FORMAT="utf-8"

while True:

	# we use this to keep a track of the possible input streams that we can have
	possible_inputs = [sys.stdin, server]

	# either a server can send a message or the user can input a message
	# select will select a reader for the input
	read_sockets,write_socket, error_socket = select.select(possible_inputs,[],[])

	for socks in read_sockets:
		# when a server is sending a message if will be true
		# when a user is giving a message as input else will be true
		if socks == server:
			message = socks.recv(2048).decode(FORMAT)
			print(message)
		else:
			message = sys.stdin.readline()
			server.send(message.encode(FORMAT))
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()
server.close()
