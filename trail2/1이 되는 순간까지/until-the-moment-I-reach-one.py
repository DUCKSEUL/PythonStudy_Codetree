cnt = 0

def _cnt(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        return _cnt(n // 2)
    else:
        cnt += 1
        return _cnt(n // 3)
    
n = int(input())
print(_cnt(n))