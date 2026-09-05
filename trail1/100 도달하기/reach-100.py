N = int(input())

arr = [1, N]
i = 0

while True:
    if arr[-1] >= 100:
        break
    arr.append(arr[i]+arr[i+1])
    i += 1

for j in arr:
    print(j, end=" ")