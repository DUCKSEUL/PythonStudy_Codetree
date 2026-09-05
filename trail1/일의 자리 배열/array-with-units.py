arr = list(map(int, input().split()))

print(f"{arr[0]} {arr[1]}", end=" ")

for i in range(8):
    arr.append((arr[i+1] + arr[i]) % 10)
    print(arr[-1], end=" ")