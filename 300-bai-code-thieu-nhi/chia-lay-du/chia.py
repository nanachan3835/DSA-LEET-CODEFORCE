N , k= map(int, input().split())

arr = map(int, input().split())

arr= map(lambda x: x % k, arr)

newarr = set(arr)

print(len(newarr))
