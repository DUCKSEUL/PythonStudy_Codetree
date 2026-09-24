a, b = map(int, input().split())

num = a + b
num_s = str(num)

cnt = 0

for i in num_s:
    if i == "1":
        cnt += 1

print(cnt)