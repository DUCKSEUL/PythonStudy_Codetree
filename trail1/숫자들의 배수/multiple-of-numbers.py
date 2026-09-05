N = int(input())

arr = []
cnt = 0

i = 0

while True:
    if cnt == 2:
        break
    arr.append(N*(i+1))
    if arr[i] % 5 == 0:
        cnt += 1
    i += 1

for j in arr:
    print(j, end=" ")