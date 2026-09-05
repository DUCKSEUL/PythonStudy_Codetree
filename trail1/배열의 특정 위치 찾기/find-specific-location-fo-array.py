arr = list(map(int, input().split()))

sum1 = []
sum2 = []

for i in range(len(arr)):
    if i % 2 == 1:
        sum1.append(arr[i])
    if (i+1) % 3 == 0:
        sum2.append(arr[i])

print(f"{sum(sum1)} {sum(sum2)/len(sum2):.1f}")