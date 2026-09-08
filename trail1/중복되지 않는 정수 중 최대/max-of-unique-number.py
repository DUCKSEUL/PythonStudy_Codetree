N = int(input())
arr = list(map(int, input().split()))

num_list = [0] * 1001

for i in range(1001):
    for num in arr:
        if i == num:
            num_list[i] += 1

idx = -1

for j in range(1000, -1, -1):
    if num_list[j] == 1:
        idx = j
        break

if idx == -1:
    print(-1)
else:
    print(j)