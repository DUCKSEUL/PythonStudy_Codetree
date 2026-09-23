s = list(input())

for i in range(len(s)):
    if s[i] == "e":
        s.pop(i)
        break

s = ''.join(s)
print(s)