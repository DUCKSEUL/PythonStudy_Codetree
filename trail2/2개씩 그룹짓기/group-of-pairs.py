n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min = -1
for i in range(n):
    sum = arr[i] + arr[len(arr)-i-1]
    if sum >= min:
        min = sum

print(min)
