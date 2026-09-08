N = int(input())
arr = list(map(int, input().split()))

d = max(arr)

for i in range(len(arr)-1):
    if arr[i+1] - arr[i] <= d:
        d = arr[i+1] - arr[i]

print(d)