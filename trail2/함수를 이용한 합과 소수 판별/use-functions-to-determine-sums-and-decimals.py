def is_cond1(n):
    temp = 0
    cnt = 0
    for i in range(1,n):
        if n % i == 0:
            cnt += 1
    if cnt == 1:
        temp = 1
    return temp

def is_cond2(n):
    temp = 0
    sum = 0
    s = str(n)
    for i in s:
        sum += int(i)
    if sum % 2 == 0:
        temp = 1
    return temp

def is_num(n):
    temp = 0
    if is_cond1(n) and is_cond2(n):
        temp = 1
    return temp

a, b = map(int, input().split())

cnt = 0
for i in range(a,b+1):
    if is_num(i):
        cnt += 1

print(cnt)