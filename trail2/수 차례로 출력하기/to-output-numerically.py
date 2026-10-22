def print_num_lower(n):
    if n == 0:
        return
    print(n, end=" ")
    print_num_lower(n-1)

def print_num_upper(n):
    if n == 0:
        return
    print_num_upper(n-1)
    print(n, end=" ")

n = int(input())
print_num_upper(n)
print()
print_num_lower(n)