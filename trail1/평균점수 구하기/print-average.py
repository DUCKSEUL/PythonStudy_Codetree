arr = list(map(float, input().split()))

sum = sum(arr)
avg = sum / len(arr)

print("%.1f" % avg)