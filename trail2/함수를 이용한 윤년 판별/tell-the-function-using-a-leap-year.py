def cal_year(n):
    cnt = 0
    if n % 100 == 0 and n % 400 != 0:
        cnt = 0
    elif n % 4 == 0:
        cnt = 1
    else:
        cnt = 0
    if cnt == 1:
        return True
    else:
        return False

a = int(input())

if cal_year(a):
    print("true")
else:
    print("false")