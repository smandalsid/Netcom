import socket

HEADER=64
PORT=2002
FORMAT="utf-8"
DISCONNECT_MESSAGE="DISCONNECT"
SERVER="192.168.43.26"
ADDR=(SERVER, PORT)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    # msg_length=len(message)
    # send_length=str(msg_length).encode(FORMAT)
    # send_length+=b' '*(HEADER-len(send_length))
    # client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

# send("Hello from same system")

while True:
    msg=input()
    if msg=="DISCONNECT":
        break
    else:
        send(msg)
# send(DISCONNECT_MESSAGE)