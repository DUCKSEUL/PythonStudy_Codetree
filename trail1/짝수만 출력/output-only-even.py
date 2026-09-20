A, B = map(int, input().split())

cnt = A

while cnt <= B:
    if cnt % 2 == 0:
        print(cnt, end=" ")
    cnt += 1