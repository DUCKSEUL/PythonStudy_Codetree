s = list(input())

s1, s2 = s[0], s[1]
for i in range(len(s)):
    if s[i] == s1:
        s[i] = s2
    elif s[i] == s2:
        s[i] = s1

s = ''.join(s)

print(s)