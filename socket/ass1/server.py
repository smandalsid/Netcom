import socket
import threading

HEADER=64
port=2002
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECT"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET is to specify the type of addresses that our socket can communicate in, in this case we are using Internet Protocol V4 addresses
# SOCK_STREAM indicates that it is a TCP socket

server.bind((SERVER, port))

def handle_client(conn, addr):
    print("New connection", end=" ")
    print(addr, end=" ")
    print("connected")

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(addr, end=" ")
            print(msg)
            conn.send("Message received".encode(FORMAT))
    conn.close()
    

def start():
    server.listen()
    print("Server is listening on", end=" ")
    print(SERVER)
    while True:
        # accepts a connection request
        conn, addr = server.accept()
        # conn is the socket object using which we can send messages back to the client
        # addr stores the IP address of the client that just connected
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Active connections", end="")
        print(threading.activeCount()-1)

print("Server is starting..")
start()