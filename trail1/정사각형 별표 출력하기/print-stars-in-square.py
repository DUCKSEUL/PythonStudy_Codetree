n = int(input())

def print_sq(a):
    if a == 0:
        return
    print_sq(a-1)
    print("*" * n)

print_sq(n)