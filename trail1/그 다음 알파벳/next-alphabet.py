s = input()

if s == 'z':
    s = 'a'
else:
    s = chr(ord(s)+1)

print(s)