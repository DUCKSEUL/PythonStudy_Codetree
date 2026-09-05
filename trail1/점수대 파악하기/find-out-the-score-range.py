raw = list(map(int, input().split()))

score = []
cnt = [0] * 11

for i in raw:
    if i == 0:
        break
    else:
        score.append(i)

for j in score:
    cnt[j // 10] += 1

for k in range(10, 0, -1):
    print(f"{10*k} - {cnt[k]}")