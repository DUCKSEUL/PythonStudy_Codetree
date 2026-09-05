N = int(input())

cnt = 0

for _ in range(N):
    arr_score = list(map(int, input().split()))
    if sum(arr_score)/len(arr_score) >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)