N, M = map(int, input().split())

num = 0

arr_num = [
    [0 for _ in range(M)]
    for _ in range(N)
]

for i in range(M):
    for j in range(N):
        if i % 2 == 0:
            arr_num[j][i] = num
            num += 1
        else:
            arr_num[N-j-1][i] = num
            num += 1

for j in range(N):
    for i in range(M):
        print(arr_num[j][i], end=" ")
    print("")