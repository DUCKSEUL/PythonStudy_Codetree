arr = list(map(int, input().split()))

num_max = 0

for i in arr:
    if i >= num_max:
        num_max = i
print(num_max)