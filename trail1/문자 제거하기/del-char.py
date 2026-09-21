s = list(input())

while len(s) > 1:
    n = int(input())
    if len(s) <= n:
        s.pop(-1)
        print(''.join(s))
    else:
        s.pop(n)
        print(''.join(s))

