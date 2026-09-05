arr_num = list(map(int, input().split()))
arr = []

for i in arr_num:
    if i == 0:
        break
    else:
        arr.append(i)

print(arr[-1] + arr[-2] + arr[-3])