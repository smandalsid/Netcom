import math
m=int(input("Enter value of m: "))
size=int(input("Enter number of packets"))
ar=[]
x=0
for i in range(size):
    if x==math.pow(2,m):
        ar.append(0)
        x=1
    else:
        ar.append(x)
        x+=1

print(ar)