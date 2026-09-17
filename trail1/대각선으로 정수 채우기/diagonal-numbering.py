N, M = map(int, input().split())

arr_num = [
    [0 for _ in range(M)]
    for _ in range(N)
]

num, idx = 1, 0
i, j = 0, 0

while num <= N * M:
    if i + j == idx:
        if (j <= M-1) and (i <= N-1):
            arr_num[i][j] = num
            num += 1
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1
    else:
        j += 1
    if j < 0:
        i = 0
        j = 0
        idx += 1

for i in range(N):
    for j in range(M):
        print(arr_num[i][j], end=" ")
    print("")