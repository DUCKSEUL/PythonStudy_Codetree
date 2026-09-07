N = int(input())

arr = list(map(int, input().split()))

arr_min = min(arr)
arr_max = max(arr)

cnt_min = 0
cnt_max = 0

for i in arr:
    if i == arr_min:
        cnt_min += 1
    elif i == arr_max:
        cnt_max += 1

print(arr_min, cnt_min)