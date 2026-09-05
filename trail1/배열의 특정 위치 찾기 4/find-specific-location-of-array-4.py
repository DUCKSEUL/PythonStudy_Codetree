arr_num = list(map(int, input().split()))
arr = []
arr_2 = []

for i in arr_num:
    if i == 0:
        break
    else:
        arr.append(i)

for j in arr:
    if j % 2 == 0:
        arr_2.append(j)

print(f"{len(arr_2)} {sum(arr_2)}")