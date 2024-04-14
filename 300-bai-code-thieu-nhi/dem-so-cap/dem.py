n,x = input().split()

count = 0
mang = input().split()

for i in range(0,len(mang)):
    for j in range(i,len(mang)):
        if int(mang[i])**2 + int(mang[j])== int(x):
            count+=1
            
print(count)