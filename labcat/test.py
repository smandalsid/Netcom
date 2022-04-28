# import math

# # ip=input("Enter IP address with subnet:\n")
# # ip="192.168.1.1/28"
# ip="172.16.0.0/25"
# iplist=ip.split('.')
# temp=iplist[-1].split('/')
# iplist[-1]=temp[0]
# iplist.append(temp[1])

# for i in range(len(iplist)):
#     iplist[i]=int(iplist[i])

# print(iplist)

# ipbinlist=[]
# for i in range(4):
#     ipbinlist.append(bin(iplist[i]))
#     ipbinlist[-1]=ipbinlist[-1][2:]
#     while len(ipbinlist[i])!=8:
#         ipbinlist[i]='0'+ipbinlist[i]


# # print(ipbinlist)

# defaultclass=''

# if ipbinlist[0][0]=='0':
#     defaultclass='a'
# elif ipbinlist[0][:2]=='10':
#     defaultclass='b'
# elif ipbinlist[0][:3]=='110':
#     defaultclass='c'
# elif ipbinlist[0][:4]=='1110':
#     defaultclass='d'
# elif ipbinlist[0][:4]=='1111':
#     defaultclass='e'

# # print(defaultclass)

# defaultmaskbits=0

# if defaultclass=='a':
#     defaultmaskbits=8
# elif defaultclass=='b':
#     defaultmaskbits=16
# elif defaultclass=='c':
#     defaultmaskbits=24

# print(defaultmaskbits)

# nsubnets=iplist[-1]-defaultmaskbits

# subnetmask=['','','','']
# subnetaddress=['','','','']

# count=iplist[-1]
# for i in range(4):
#     for j in range(8):
#         if count>0:
#             subnetmask[i]+='1'
#             count-=1
#         else:
#             subnetmask[i]+='0'
#         subnetaddress[i]+=str(int(ipbinlist[i][j])&int(subnetmask[i][-1]))

# print(subnetmask)
# print(subnetaddress)

# broadcastaddress=['', '', '', '']
# count=iplist[-1]
# for i in range(4):
#     for j in range(8):
#         if count>0:
#             broadcastaddress[i]+=ipbinlist[i][j]
#             count-=1
#         else:
#             broadcastaddress[i]+='1'

        
# # print("Number of subnets: "+str(nsubnets))
# print(broadcastaddress)

# nhpersubnet=2**(32-iplist[-1])-2
# print(nhpersubnet)

# for i in range(len(ipbinlist)):
#     print(int(ipbinlist[i], 2))

import math

ip="172.16.0.0/25"

iplist=ip.split('.')
temp=iplist[-1].split('/')
iplist[-1]=temp[0]
iplist.append(temp[1])

for i in range(len(iplist)):
    iplist[i]=int(iplist[i])

ipbinlist=[]
for i in range(len(iplist)-1):
    ipbinlist.append(bin(iplist[i]))
    ipbinlist[-1]=ipbinlist[-1][2:]
    while len(ipbinlist[-1])!=8:
        ipbinlist[-1]='0'+ipbinlist[-1]

defaultclass=""
if ipbinlist[0][0]=='0':
    defaultclass='a'
elif ipbinlist[0][:2]=='10':
    defaultclass='b'
elif ipbinlist[0][:3]=='110':
    defaultclass='c'

if defaultclass=='a':
    defaultmask=8
elif defaultclass=='b':
    defaultmask=16
else:
    defaultmask=24

subnetmask=['', '', '', '']
count=iplist[-1]

for i in range(4):
    for j in range(8):
        if count>0:
            subnetmask[i]+='1'
            count-=1
        else:
            subnetmask[i]+='0'

subnetaddress=['', '', '', '']
for i in range(4):
    for j in range(8):
        subnetaddress[i]+=str(int(ipbinlist[i][j])&int(subnetmask[i][j]))
fsubnetaddress=''
for i in range(4):
    fsubnetaddress=fsubnetaddress+str(int(subnetaddress[i], 2))+'.'

fsubnetaddress=fsubnetaddress[:len(fsubnetaddress)-1]

broadcastaddress=['', '', '' ,'']
count=iplist[-1]
for i in range(4):
    for j in range(8):
        if count>0:
            broadcastaddress[i]+=ipbinlist[i][j]
            count-=1
        else:
            broadcastaddress[i]+='1'

fbroadcastaddress=''
for i in range(4):
    fbroadcastaddress=fbroadcastaddress+str(int(broadcastaddress[i], 2))+'.'
fbroadcastaddress=fbroadcastaddress[:len(fbroadcastaddress)-1]

print("Number of subnets: "+str(2**(iplist[-1]-defaultmask)))
print("Number of hosts per subnet: "+str(2**(32-iplist[-1])-2))
print("Subnet address: ", fsubnetaddress)
print("Broadcast address: ", fbroadcastaddress)

subnetlist=fsubnetaddress.split('.')
subnetlist[-1]=str(int(subnetlist[-1])+1)
firsthostid="".join(x+'.' for x in subnetlist)
firsthostid=firsthostid[:len(firsthostid)-1]
subnetlist[-1]=str(int(subnetlist[-1])+2**(32-iplist[-1])-2-1)
lasthostid="".join(x+"." for x in subnetlist)
lasthostid=lasthostid[:len(lasthostid)-1]


print("First host id in first subnet block: ", firsthostid)
print("Last host id in first subnet block: ", lasthostid)
