
n=int(input())

while True:
    if n%2==0:
        print(n,end=" ")
        n=int(n/2)
    elif n==1:
        print(n,end=" ")
        break
    else:
        print(n,end=" ")
        n=int(3*n+1)

        