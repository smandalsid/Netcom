address=input()

l=address.split('.')

temp=l[-1].split('/')
l[-1]=temp[0]
l.append(temp[1])

binary=[]

for i in range(len(l)):
    l[i]=int(l[i])

for i in range(len(l)-1):
    if l[i]>=0 and l[i]<=255:
        binary.append(bin(l[i])[2:])
    else:
        print("Invalid address address")
        exit()

for i in range(len(l)-1):
    while len(binary[i])<8:
        binary[i]='0'+binary[i]

addressclass=''

if binary[0]=='0':
    addressclass="A"
elif binary[0][0:2]=="10":
    addressclass="B"
elif binary[0][0:3]=="110":
    addressclass="C"
elif binary[0][0:4]=="1110":
    addressclass="D"
elif binary[0][0:4]=="1111":
    addressclass="E"
    

print("Class of the given address address: ", addressclass)

if addressclass=="A":
    nbdm=8
elif addressclass=="B":
    nbdm=16
elif addressclass=="C":
    nbdm=24

nsubnets=2**(l[-1]-nbdm)

print("Number of subnets: ", nsubnets)

nhpersubnet=(2**(32-l[-1]))-2
print("Number of hosts per subnet: ", nhpersubnet)

zeroes=32-l[-1]
counter=0

for i in range(len(l)-2, -1, -1):
    if zeroes>=8:
        binary[i]="00000000"
        zeroes-=8
    else:
        binary[i]=binary[i][:8-zeroes]
        while zeroes>0:
            binary[i]+='0'
            zeroes-=1

# print(binform)

subnet_address=[]

for i in range(len(binary)):
    # temp="0b"+binform[i]
    subnet_address.append(int(binary[i], 2))

    # if i != len(binform)-1:
    #     subnet_address+="."


temp=""
for i in range(len(subnet_address)):
    temp+=str(subnet_address[i])
    if i!=len(subnet_address)-1:
        temp+="."

print(temp)

temp1=""
temp2=""
for i in range(len(subnet_address)):
    if i == len(subnet_address)-1:
        temp1+=str(subnet_address[i]+1)
        temp2+=str(subnet_address[i]+nhpersubnet+1)
    else:
        temp1+=str(subnet_address[i])
        temp2+=str(subnet_address[i])
    if i!=len(subnet_address)-1:
        temp1+='.'
        temp2+='.'

print(temp1, temp2)
