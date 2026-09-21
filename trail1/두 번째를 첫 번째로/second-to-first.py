s = tuple(input())

new_s = []
s1 = s[0]
s2 = s[1]


for i in range(len(s)):
    if s[i] == s2:
        new_s.append(s1)
    else:
        new_s.append(s[i])

new_s = ''.join(new_s)

print(new_s)