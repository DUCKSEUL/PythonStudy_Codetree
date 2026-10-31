n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

lt = len(t)
str_new = []
for i in str:
    if i[:lt] == t:
        str_new.append(i)

str_new.sort()

print(str_new[k-1])