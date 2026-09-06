arr = list(map(int, input().split()))
arr_num = list(map(int, input().split())) 

cnt = 0

for i in range(arr[0]):
    if arr[1] == arr_num[i]:
        cnt += 1

print(cnt)