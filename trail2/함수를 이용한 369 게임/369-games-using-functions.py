def is_have_369(n):
    bool = False
    str_n = str(n)
    for i in str_n:
        if i == "3" or i == "6" or i == "9":
            bool = True
    return bool

def is_magic_number(n):
    return n % 3 == 0 or is_have_369(n)

a, b = map(int, input().split())

cnt = 0
for i in range(a,b+1):
    if is_magic_number(i):
        cnt += 1

print(cnt)