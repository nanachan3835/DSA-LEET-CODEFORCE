import math

n,m,k=input().split()
n,m,k=int(n),int(m),int(k)
a=[]
a=a+input().split()
dem=0
met=1000000000
for i in range(0,n):
    if int(a[i]) <= k and int(a[i]) != 0:
        met = min(met,(abs(i-(m-1))))
        dem+=1

if dem==0:
    print(-1)
else:
    print(met*10)