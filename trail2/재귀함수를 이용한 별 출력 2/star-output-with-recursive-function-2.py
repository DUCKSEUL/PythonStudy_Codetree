def print_tower_star(n):
    if n == 0:
        return
    print("* " * n)
    print_tower_star(n-1)
    print("* " * n)

n = int(input())
print_tower_star(n)