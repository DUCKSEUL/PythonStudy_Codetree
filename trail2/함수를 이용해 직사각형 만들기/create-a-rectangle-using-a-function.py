def make_sq(N, M):
    for i in range(N):
        for j in range(M):
            print(1, end="")
        print("")

n, m = map(int, input().split())

make_sq(n, m)