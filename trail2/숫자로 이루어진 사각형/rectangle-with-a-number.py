def draw_sq_1(N):
    cnt = 1
    for i in range(N):
        for j in range(N):
            if cnt == 10:
                cnt = 1
            print(cnt, end=" ")
            cnt += 1
        print("")

n = int(input())

draw_sq_1(n)