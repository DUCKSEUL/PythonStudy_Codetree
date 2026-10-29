n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr.append(s)

arr.sort()
for i in arr:
    print(i)