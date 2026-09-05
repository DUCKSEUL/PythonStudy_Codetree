arr = list(map(int, input().split()))

new_arr = []

for i in range(len(arr)):
    if arr[i] <= 250:
        new_arr.append(arr[i])
    else:
        break

sum = 0
for j in range(len(new_arr)):
    sum += new_arr[j]

print(f"{sum} {sum/len(new_arr):.1f}")