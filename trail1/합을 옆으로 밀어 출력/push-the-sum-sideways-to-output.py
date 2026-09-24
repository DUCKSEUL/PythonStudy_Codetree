N = int(input())

sum = 0

for _ in range(N):
    a = int(input())
    sum += a

sum = str(sum)
sum = sum[1:] + sum[0]

print(sum)