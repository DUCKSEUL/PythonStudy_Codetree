def is_minor(n):
    cnt = True
    for i in range(2, n):
        if n % i == 0:
            cnt = False
    return cnt

a, b = map(int, input().split())

sum = 0
for i in range(a, b+1):
    if is_minor(i):
        sum += i
print(sum)