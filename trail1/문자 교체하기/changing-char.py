s = tuple(input().split())

s1 = list(s[0])
s2 = list(s[1])

s2[:2] = s1[:2]

s1 = ''.join(s1)
s2 = ''.join(s2)

print(s2)