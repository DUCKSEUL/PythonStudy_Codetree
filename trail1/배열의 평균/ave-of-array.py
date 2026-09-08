arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))

for i in range(2):
    print(f"{sum(arr[i])/len(arr[i]):.1f}", end=" ")
print("")

for j in range(4):
    print(f"{(arr[0][j]+arr[1][j])/2:.1f}", end=" ")
print("")

arr_sum = 0
for k in range(2):
    arr_sum += sum(arr[k])
print(f"{arr_sum/8:.1f}")