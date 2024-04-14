import math

def solve(n):
    for i in range(int(math.sqrt(n)),0,-1):
        ans = int(n/i)
        if ans*i == n:
            return i, ans
        
    return 0,0


for i in range(int(input())):
    a,b= solve(int(input()))
    print(f"{a} {b}")