num = 1

arr_num = list(map(int, input().split()))
arr_2d = [
    [0 for _ in range(arr_num[1])]
    for _ in range(arr_num[0])
]

for i in range(arr_num[0]):
    for j in range(arr_num[1]):
        arr_2d[i][j] = num
        print(num, end=" ")
        num += 1
    print("")