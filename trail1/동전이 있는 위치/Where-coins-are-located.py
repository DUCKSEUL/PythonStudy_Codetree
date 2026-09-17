N, M = map(int, input().split())

cat = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for _ in range(M):
    x, y = map(int, input().split())
    cat[x-1][y-1] = 1

for i in range(N):
    for j in range(N):
        print(cat[i][j], end=" ")
    print("")