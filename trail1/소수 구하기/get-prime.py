N = int(input())

cnt = 0

for i in range(1, N+1):
    cnt_dot = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt_dot += 1
    if cnt_dot == 2:
        print(j, end=" ")