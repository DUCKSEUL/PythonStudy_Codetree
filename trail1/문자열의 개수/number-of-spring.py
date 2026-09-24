cnt = 0
s_string = []

while True:
    s = input()
    if s == "0":
        break
    cnt += 1
    if cnt % 2 == 1:
        s_string.append(s)

print(cnt)

for i in s_string:
    print(i)