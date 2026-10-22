a = input()
b = input()
la, lb = len(a), len(b)

def is_in_a():
    for i in range(la-lb+1):
        if a[i:(i+lb):1] == b:
            return i
    return -1

print(is_in_a())