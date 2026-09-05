arr = []

num_arr = list(map(int, input().split()))
for i in num_arr:
    if i == 0:
        break
    else:
        arr.append(i)

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")