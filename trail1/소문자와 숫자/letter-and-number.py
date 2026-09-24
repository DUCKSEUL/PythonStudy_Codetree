s = input()

for i in s:
    if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')):
        print(i.lower(), end="")
    elif (ord('0') <= ord(i) <= ord('9')):
        print(i, end="")