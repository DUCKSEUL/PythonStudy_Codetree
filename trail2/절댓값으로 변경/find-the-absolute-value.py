def change_abs(arr):
    arr_new = []
    for i in arr:
        if i >= 0:
            arr_new.append(i)
        else:
            arr_new.append(i*(-1))
    return(arr_new)

n = int(input())
arr = list(map(int, input().split()))

arr = change_abs(arr)

for i in arr:
    print(i, end=" ")