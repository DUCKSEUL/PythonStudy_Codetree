s = input()

for i in s:
    if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')):
        print(i.upper(), end="")
        # i.upper()
        # print(i, end="")
