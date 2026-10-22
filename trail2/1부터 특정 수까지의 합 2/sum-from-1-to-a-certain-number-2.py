def _sum(n):
    if n == 1:
        return 1
    return _sum(n-1) + n

n = int(input())
print(_sum(n))