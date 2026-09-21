input_str = input()
target_str = input()

len_in = len(input_str)
len_t = len(target_str)

cnt = 0

for i in range(len_in - len_t + 1):
    s = ""
    for j in range(len_t):
        s = s + input_str[i+j]
    if s == target_str:
        print(i)
        cnt += 1
        break

if cnt == 0:
    print(-1)