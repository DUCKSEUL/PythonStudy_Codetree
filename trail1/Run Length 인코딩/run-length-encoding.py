s = input()

new_arr = []
now_cnt = 0
run_length = ""

for i, elem in enumerate(s):
    now_str = elem
    if now_cnt == 0:
        new_arr.append(elem)
        now_cnt += 1
    else:
        if new_arr[-1] == now_str:
            now_cnt += 1
        else:
            new_arr.append(now_cnt)
            now_cnt = 1
            new_arr.append(now_str)
    if i == len(s)-1:
        new_arr.append(now_cnt)

for i in new_arr:
    run_length += str(i)

print(len(run_length))
print(run_length)