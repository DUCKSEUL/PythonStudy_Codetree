def pbnc(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return pbnc(n-1) + pbnc(n-2)

n = int(input())
print(pbnc(n))