N = int(input())

arr = [
    input()
    for _ in range(N)
]

len_arr = 0
cnt = 0

for i in range(len(arr)):
    len_arr += len(arr[i])
    if arr[i][0] == "a":
        cnt += 1

print(len_arr, cnt)