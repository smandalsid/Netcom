import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP=socket.gethostbyname(socket.gethostname())

FORMAT="utf-8"
PORT=2005

server.bind((SERVER_IP, PORT))
server.listen(100)

def handle_client(conn, addr):
    conn.send("Welcome to this chat".encode(FORMAT))
    while True:
        try:
            print(conn.recv(2048).decode(FORMAT))
            msg=input()
            conn.send(msg.encode(FORMAT))
        except:
            continue



def start():
    print("[STARTING] Server is starting")
    print("IP address of the server: "+SERVER_IP)
    print("[LISTENING] listening for connections")
    conn, addr=server.accept()
    print("[CONNECTED] IP address of client: "+str(addr[0])+" port: "+str(addr[1]))
    handle_client(conn, addr)

start()