n =int(input())

m = input().split()

tongchan=0
tongle=0

for i in range(len(m)):
    if int(i)%2==0:
        tongle+=int(m[i])
    else:  
        tongchan+=int(m[i])

print(tongchan-tongle)    