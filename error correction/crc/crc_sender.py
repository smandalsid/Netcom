import socket

port=2010
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, port))


# to send the data to the receiver
def handle_client(conn, addr):

    # taking the dataword and the divisor from the user
    data=input("Enter your binary dataword:\n")
    divisor=input("Enter the divisor:\n")
    codeword=data
    l=len(divisor)

    # adding length of divisor -1 number of zeroes to the dataword
    for i in range(l-1):
        data+='0'

    print("Data word after adding zeros:", data)

    # getting the checksum value
    addition=division(data, divisor, l)
    print("CRC chechsum value: ", addition)

    # generating the codeword
    codeword+=addition
    print("Codeword generated: ", codeword)

    print(conn.recv(2048).decode(FORMAT))

    # two manually set codewords to simulate error in transmission condition
    error="10100111001010"
    error2="1111110"

    # sending the codeword
    conn.send(error.encode(FORMAT))
    print("Codeword sent to receiver")
    # sending the divisor
    conn.send(divisor.encode(FORMAT))
    print("Divisor sent to receiver")

#  it will generate the checksum value
def division(data, divisor, l):
    rem=""
    while len(data)>=len(divisor):
        a=data[:l]
        temp=xor(a, divisor)
        data=temp+data[l:]
    return data

# to generate the XOR value at each step of the division
def xor(a, b):
    temp=""
    for i in range(len(a)):
        if a[i]==b[i]:
            temp+='0'
        else:
            temp+='1'
    ans=temp
    for i in range(len(temp)-1):
        if temp[i]=='0':
            ans=temp[i+1:]
        else:
            break

    return ans


def start():
    print("\n****** SIDDHARTH MANDAL ******")
    print("****** REG. NO. 20BDS0157 ******\n")
    # listening for a connection
    server.listen(1)
    print("[STARTING] Sender is ready...")
    print("[LISTENING] Listening for a connection... ")
    # accept a connection
    conn, addr=server.accept()
    print("[REQUEST] Connecting...")
    print("[CONNECTED] IP address of receiver: "+str(addr[0])+" at PORT: "+str(addr[1]))
    handle_client(conn, addr)

    conn.close()
    server.close()

start()
