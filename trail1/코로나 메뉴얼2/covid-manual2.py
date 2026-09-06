cnt = [0] * 5

for _ in range(3):
    people = list(input().split())
    if int(people[1]) >= 37:
        if people[0] == "Y":
            cnt[1] += 1
        else:
            cnt[2] += 1
    else:
        if people[0] == "Y":
            cnt[3] += 1
        else:
            cnt[4] += 1

for i in range(1, 5):
    print(cnt[i], end=" ")
if cnt[1] >= 2:
    print("E")