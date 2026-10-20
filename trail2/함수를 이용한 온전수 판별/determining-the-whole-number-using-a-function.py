def is_clean_num(i):
    temp = 1
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        temp = 0
    return temp

cnt = 0
a, b = map(int, input().split())
for i in range(a,b+1):
    if is_clean_num(i):
        cnt += 1

print(cnt)