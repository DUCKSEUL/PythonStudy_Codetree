def _sum(n):
    if n % 2 == 1:
        if n == 1:
            return 1
        else:
            return _sum(n-2) + n
    else:
        if n == 2:
            return 2
        else:
            return _sum(n-2) + n

n = int(input())
print(_sum(n))