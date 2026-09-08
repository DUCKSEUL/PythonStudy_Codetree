N = int(input())
arr = list(map(int, input().split()))

idx = -1

while True:
    if idx == 0:
        break
    for i, num in enumerate(arr):
        if num == max(arr):
            print(i+1, end=" ")
            idx = i
            arr = arr[0:i]
            break