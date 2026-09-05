N = int(input())

cnt = 1
for i in range(N):
    for j in range(N):
        if cnt >= 10:
            cnt = 1
        if i > j:
            print(" ", end=" ")
        else:
            print(cnt, end=" ")
            cnt += 1
    print("")