arr = []

num_arr = list(map(int, input().split()))

for i in num_arr:
    if i == 0:
        break
    else:
        arr.append(i)

print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")