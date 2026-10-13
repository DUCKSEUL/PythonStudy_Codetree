def print_sq(a,b):
    prod = 1
    for _ in range(b):
        prod *= a
    return prod

a, b = map(int, input().split())
ans = print_sq(a,b)
print(ans)