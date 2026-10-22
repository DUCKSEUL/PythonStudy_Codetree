n, m = map(int, input().split())
a = list(map(int, input().split()))

arr_m = [m]

def split_m():
    global m
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1

while m != 1:
    split_m()
    arr_m.append(m)

sum = 0
for i in arr_m:
    sum += a[i-1]

print(sum)