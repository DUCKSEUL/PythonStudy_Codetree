s = tuple(input().split())

cnt = 0

for i in range(len(s[0])):
    if s[0][i] == s[1]:
        print(i)
        cnt += 1
        break
if cnt == 0:
    print("No")