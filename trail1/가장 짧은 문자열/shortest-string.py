s = []
for _ in range(3):
    s.append(input())

arr_len = []

for elem in s:
    arr_len.append(len(elem))

print(max(arr_len)-min(arr_len))