arr = list(map(int, input().split()))

num = [0] * 7

for i in arr:
    num[i] += 1

for j in range(1,7):
    print(f"{j} - {num[j]}")