num = list(map(int, input().split()))

arr = []

cnt = [0] * 10

for i in num:
    if i == 0:
        break
    else:
        arr.append(i)

for j in arr:
    cnt[j // 10] += 1

for k in range(1, 10):
    print(f"{k} - {cnt[k]}")