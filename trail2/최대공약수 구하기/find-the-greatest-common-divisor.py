def cal_common_div(n, m):
    div = 0
    if n >= m:
        for i in range(1, m+1):
            if (n % i == 0) and (m % i == 0):
                div = i
    else:
        for i in range(1, n+1):
            if (n % i == 0) and (m % i == 0):
                div = i
    
    print(div)

m, n = map(int, input().split())
cal_common_div(n, m)