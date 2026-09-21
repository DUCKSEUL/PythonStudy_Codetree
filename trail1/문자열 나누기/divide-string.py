N = int(input())
arr = tuple(input().split())

cnt = 0

s = ""

for i in arr:
    s = s + i

for i in s:
    if cnt == 5:
        cnt = 0
        print("")
    print(i, end="")
    cnt += 1