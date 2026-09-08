arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))

for k in arr:
    print(sum(k))