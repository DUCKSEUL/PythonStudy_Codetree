arr = list(map(int, input().split()))

cnt_partial = [0] * 11

while True:
    if arr[0] <= 1:
        break
    temp = arr[0]

    all = arr[0] // arr[1]
    partial = arr[0] % arr[1]

    arr[0] = all
    cnt_partial[partial] += 1

sum = 0

for i in cnt_partial:
    sum += i**2

print(sum)