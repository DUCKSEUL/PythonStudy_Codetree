arr = list(map(int, input().split()))

arr_o = []
arr_e = []

for i in range(len(arr)):
    if i % 2 == 0:
        arr_o.append(arr[i])
    else:
        arr_e.append(arr[i])

if sum(arr_o) >= sum(arr_e):
    print(sum(arr_o)-sum(arr_e))
else:
    print(sum(arr_e)-sum(arr_o))