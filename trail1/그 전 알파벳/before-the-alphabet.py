s = input()

if s == "a":
    s = "z"
else:
    s = chr(ord(s) - 1)

print(s)