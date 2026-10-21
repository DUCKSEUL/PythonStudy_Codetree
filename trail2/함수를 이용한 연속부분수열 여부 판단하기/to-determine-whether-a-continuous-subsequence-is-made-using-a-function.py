def is_corr_arr(a,b):
    la, lb = len(a), len(b)
    temp = False
    for i in range(la-lb+1):
        temp_s = []
        for j in range(lb):
            temp_s.append(a[i+j])
        if temp_s == b:
            temp = True
    return temp

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print("Yes" if is_corr_arr(a,b) else "No")