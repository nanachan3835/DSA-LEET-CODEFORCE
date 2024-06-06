import math

N =int(input())

def anwer(N):
    string = []
    for i in range(2,int(math.sqrt(N+1))):
        if N % i == 0:
            string.append(i)
            while N % i == 0:
                N = N /i
      
    return string


n= anwer(N)
print("*".join(map(str, filter(None, n))))
    

                