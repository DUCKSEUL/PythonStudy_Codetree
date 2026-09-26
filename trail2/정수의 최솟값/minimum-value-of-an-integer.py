a, b, c = map(int, input().split())

def def_min_num(a, b, c):
    if (a <= b) and (a <= c):
        return a
    elif (b <= a) and (b <= c):
        return b
    else:
        return c

num_min = def_min_num(a, b, c)

print(num_min)