s = input()
word = input()
cnt = 0

for i in range(len(s)):
    if s[i] == word:
        cnt += 1

print(cnt)