N = int(input())
arr = list(map(int, input().split()))

arr_new = []

idx = 0
for i, num in enumerate(arr):
    if arr[i] == max(arr):
        idx = i

for j in range(len(arr)):
    if j != idx:
        arr_new.append(arr[j])

print(max(arr), max(arr_new))