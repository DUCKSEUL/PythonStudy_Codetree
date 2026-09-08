arr = list(map(int, input().split()))

arr_small = []
arr_large = []

for num in arr:
    if num < 500:
        arr_small.append(num)
    elif num > 500:
        arr_large.append(num)

print(max(arr_small), min(arr_large))