N = int(input())
arr = list(map(int, input().split()))

loss = 0
max_diff = 0

for i in range(N-1):
    if arr[i] - arr[i+1] >= 0:
        loss += 1

if loss == N-1:
    print(0)
else:
    for i in range(N):
        for j in range(i, N):
            if (arr[i] <= arr[j]) and (arr[j] - arr[i] >= max_diff):
                max_diff = arr[j] - arr[i]
    print(max_diff)