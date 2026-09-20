arr = [
    input()
    for _ in range(10)
]
word = input()

cnt = 0

for i in range(len(arr)):
    if arr[i][-1] == word:
        cnt += 1
        print(arr[i])

if cnt == 0:
    print("None")