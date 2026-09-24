a = input()

for i in a:
    if (ord("a") <= ord(i) <= ord("z")):
        print(i.upper(), end="")
    elif (ord("A") <= ord(i) <= ord("Z")):
        print(i.lower(), end="")