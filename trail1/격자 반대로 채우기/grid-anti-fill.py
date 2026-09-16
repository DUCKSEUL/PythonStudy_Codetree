num = 1
N = int(input())

arr_num = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            arr_num[N-j-1][N-i-1] = num
            num += 1
        else:
            arr_num[j][N-i-1] = num
            num += 1

for i in range(N):
    for j in range(N):
        print(arr_num[i][j], end=" ")
    print("")
