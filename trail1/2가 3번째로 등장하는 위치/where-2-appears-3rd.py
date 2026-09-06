N = int(input())

arr = list(map(int, input().split()))
cnt = 0
idx = 0

for i, num in enumerate(arr):
    if cnt == 3:
        break
    if num == 2:
        cnt += 1
        idx = i

print(idx+1)