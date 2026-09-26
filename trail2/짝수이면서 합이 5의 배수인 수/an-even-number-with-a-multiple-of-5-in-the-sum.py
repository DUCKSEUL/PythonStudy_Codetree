n = int(input())

def sort_num(n):
    return (n % 2 == 0) and ( ((n // 10) + (n % 10)) % 5 == 0)

if sort_num(n):
    print("Yes")
else:
    print("No")