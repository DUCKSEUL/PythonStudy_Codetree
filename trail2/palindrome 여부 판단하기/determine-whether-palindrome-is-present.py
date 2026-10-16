def flip(str):
    a = str
    b = str[::-1]
    if a == b:
        return 1
    else:
        return 0

a = input()
num = flip(a)
print("Yes" if num == 1 else "No")