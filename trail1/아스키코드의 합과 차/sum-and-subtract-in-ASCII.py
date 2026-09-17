arr_s = list(input().split())
arr = list(map(ord, arr_s))

pl = arr[0] + arr[1]
if arr[0] >= arr[1]:
    mi = arr[0] - arr[1]
else:
    mi = arr[1] - arr[0]

print(pl, mi)