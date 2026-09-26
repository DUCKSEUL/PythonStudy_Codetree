n = int(input())

def cal(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return (sum // 10)

n_cal = cal(n)

print(n_cal)