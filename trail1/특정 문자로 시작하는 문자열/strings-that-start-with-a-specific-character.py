N = int(input())

arr = [
    input()
    for _ in range(N)
]
word = input()

len_t = 0
cnt = 0

for i in range(len(arr)):
    if arr[i][0] == word:
        cnt += 1
        len_t += len(arr[i])
    
print(f"{cnt} {len_t/cnt:.2f}")