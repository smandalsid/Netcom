
print("")
print("")
print("Name: SIDDHARTH MANDAL")
print("Reg. No.: 20BDS0157")
print("")
print("")

print("Enter the IP address, with the mask value:")
ip=input()

# get the divisions of the IP address
l=ip.split('.')

# get the mask value
temp=l[-1].split('/')
l[-1]=temp[0]
l.append(temp[1])

binform=[]

for i in range(len(l)):
    l[i]=int(l[i])

# get the binary form of the IP address
for i in range(len(l)-1):
    if l[i]>=0 and l[i]<=255:
        binform.append(bin(l[i])[2:])
    else:
        print("Invalid IP address")
        exit()

# set every division as 8 bits for the IP address
for i in range(len(l)-1):
    while len(binform[i])<8:
        binform[i]='0'+binform[i]

ipclass=''

# find the class for the entered IP address
if binform[0]=='0':
    ipclass="A"
elif binform[0][0:2]=="10":
    ipclass="B"
elif binform[0][0:3]=="110":
    ipclass="C"
elif binform[0][0:4]=="1110":
    ipclass="D"
elif binform[0][0:4]=="1111":
    ipclass="E"
    

# priny the class of the IP address
print("Class of the given IP address: ", ipclass)

if ipclass=="A":
    nbdm=8
elif ipclass=="B":
    nbdm=16
elif ipclass=="C":
    nbdm=24

# find the number of subnets
nsubnets=2**(l[-1]-nbdm)

# print the number of subnets
print("Number of subnets: ", nsubnets)

# find the number of hosts per subnet
nhpersubnet=(2**(32-l[-1]))-2
print("Number of hosts per subnet: ", nhpersubnet)

# find how many bits from the end we have to make according to the mask value
zeroes=32-l[-1]
counter=0

# set the 32-mask bits from the right as 0 to get the subnet address
for i in range(len(l)-2, -1, -1):
    if zeroes>=8:
        binform[i]="00000000"
        zeroes-=8
    else:
        binform[i]=binform[i][:8-zeroes]
        while zeroes>0:
            binform[i]+='0'
            zeroes-=1


subnet_address=[]
# convert to decimal form from binary to find the subnet address in the next step
for i in range(len(binform)):
    subnet_address.append(int(binform[i], 2))


temp=""
# find the subnet address
for i in range(len(subnet_address)):
    temp+=str(subnet_address[i])
    if i!=len(subnet_address)-1:
        temp+="."

print("Subnet address: ", temp)

temp1=""
temp2=""
# get the first host id and the last host id.
# we add one to the subnet address for the first host id and add the number of hosts per subnet to get the last host id
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


# printing the first and the last host id
print("First host id: ", temp1)
print("Last host id: ", temp2)