N, M = map(int, input().split())

arr = []
cat = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for _ in range(M):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(M):
            if (i+1 == arr[k][0]) and (j+1 == arr[k][1]):
                cat[i][j] = (i+1)*(j+1)
        print(cat[i][j], end=" ")
    print("")