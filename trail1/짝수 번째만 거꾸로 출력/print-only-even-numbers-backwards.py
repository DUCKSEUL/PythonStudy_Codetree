s = input()

a = []

for i in range(len(s)):
    if i % 2 != 0:
        a.append(s[i])

for j in range(len(a)):
    print(a[len(a)-1-j], end="")