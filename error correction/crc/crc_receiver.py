import socket

print("")
print("** NAME: SIDDHARTH MANDAL **")
print("** REG NO. 20BDS0157 **")
print("")
rec=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SENDER="192.168.1.5"
FORMAT="utf-8"
PORT=2010

print("[CONNECTING] Conneting with the sender...")
# connect with the sender
rec.connect((SENDER, PORT))
print("Connected...")

rec.send("RECEIVER: READY to receive...".encode(FORMAT))

# receive the codeword from the sender
codeword=rec.recv(2048).decode(FORMAT)
print("Codeword received: ", codeword)
# receive the divisor from the sender
divisor=rec.recv(2048).decode(FORMAT)
print("Divisor received: ", divisor)
l=len(divisor)


# find the syndrome using the divisor and the codeword
def division(data, divisor, l):
    rem=""
    while len(data)>=len(divisor):
        a=data[:l]
        temp=xor(a, divisor)
        data=temp+data[l:]
    return data

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

syndrome=division(codeword, divisor, l)
while len(syndrome)!=4:
    syndrome='0'+syndrome
print("Syndrome: ", syndrome)

# if the syndrome is 0, the codeword received is accepted else rejected
for i in syndrome:
    if i!='0':
        print("Dataword discarded...")
        rec.close()
        exit(0)

print("Dataword accepted...")
rec.close()