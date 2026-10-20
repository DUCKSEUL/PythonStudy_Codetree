a = input()
b = input()

while True:
    cnt = 0
    la, lb = len(a), len(b)
    temp = ""
    for i in range(la-lb+1):
        for j in range(lb):
            temp += a[i+j]
        if temp == b:
            cnt = 1
            a = a[:i] + a[(i+lb):]
        else:
            temp = ""
        if cnt == 1:
            break
    if cnt == 0:
        break

print(a)