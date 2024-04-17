N = int(input())

arr = input().split()
tong=0
for i in range(N):
    if int(arr[i]) % 2 != 0:
        tong += int(arr[i])
        
    
print(tong)
         

# # N = int(input())

# arr = input().split()
# arr = map(int, arr)
# dem=0
# for i in range(N):
#     if arr[i] % 2 != 0:
#         dem += 1
    
# print(dem)
         