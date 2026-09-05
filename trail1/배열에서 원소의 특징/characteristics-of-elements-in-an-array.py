arr = list(map(int, input().split()))

arr_3 = []

for i in arr:
    if i % 3 == 0:
        break
    else:
        arr_3.append(i)

print(arr_3[-1])