N = int(input())

cnt = [0] * 9

arr_num = list(map(int, input().split()))

for i in range(1, 10):
    for j in arr_num:
        if i == j:
            cnt[i-1] += 1

for k in cnt:
    print(k)