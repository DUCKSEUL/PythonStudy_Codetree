N = int(input())

arr_num = list(map(int, input().split()))
arr_p = []

for i in arr_num:
    if i % 2 == 0:
        arr_p.append(i)

for j in range(len(arr_p)-1, -1, -1):
    print(arr_p[j], end=" ")