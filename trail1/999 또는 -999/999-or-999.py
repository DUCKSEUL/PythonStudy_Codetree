arr = list(map(int, input().split()))
arr_new = arr[0:len(arr)-1]

print(max(arr_new), min(arr_new))