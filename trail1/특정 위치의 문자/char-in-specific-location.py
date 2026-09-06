word = ['L', 'E', 'B', 'R', 'O', 'S']

N = input()
cnt = 0
idx = -1

for i, char in enumerate(word):
    if char == N:
        cnt += 1
        idx = i

if cnt == 1:
    print(idx)
else:
    print("None")