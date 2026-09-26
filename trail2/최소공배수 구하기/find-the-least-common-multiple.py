n, m = map(int, input().split())

def cal_common_val(n, m):
    cnt = 0
    i = 1
    while True:
        if (i % n == 0) and (i % m == 0):
            cnt += 1
        if cnt == 1:
            break
        i += 1
    
    print(i)

cal_common_val(n, m)