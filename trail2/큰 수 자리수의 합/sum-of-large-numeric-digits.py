def mult(n):
    if n // 10 == 0:
        return n
    return mult(n // 10) + n % 10

arr = list(map(int, input().split()))
prod = 1
for i in arr:
    prod *= i

print(mult(prod))