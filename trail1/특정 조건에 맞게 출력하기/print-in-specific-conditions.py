arr_num = list(map(int, input().split()))

arr = []

for i in arr_num:
    if i == 0:
        break
    else:
        arr.append(i)

for j in arr:
    if j % 2 != 0:
        print(j + 3, end=" ")
    else:
        print(j // 2, end=" ")