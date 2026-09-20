s = input()
n = int(input())

ls = len(s)

if n > ls:
    for i in range(ls):
        print(s[ls-1-i],end="")
else:
    for i in range(n):
        print(s[ls-1-i], end="")