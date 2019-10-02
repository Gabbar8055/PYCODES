# cook your dish here
nxy=input().split()
n=int(nxy[0])
x=int(nxy[1])
y=int(nxy[2])

'''
a=[0]*n
b=[0]*n '''

d=[0]*100001
s=0
a1=input().split()
a=list(map(int , a1))
b1=input().split()
b=list(map(int , b1))
c=[0]*len(b)
for i in range(n):
    c[i]=a[i]-b[i]
    s+=b[i]

c.sort()
for i in range(n):
    d[i]=c[n-i-1]

for i in range(n-y):
    s+=d[i]

sub=0
for i in range(n-y,x):
    if d[i]>0:
        sub+=d[i]
    else:
        break
s+=sub
print(s)

    
