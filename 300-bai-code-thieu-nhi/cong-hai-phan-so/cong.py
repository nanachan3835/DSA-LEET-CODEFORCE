import math 

abcd = input().split()

a,b,c,d = list(map(int,abcd))


f=b*d
e=a*d+b*c

divisor = math.gcd(e,f)

e = int(e/divisor)
f = int(f/divisor) 

print(e,f)


