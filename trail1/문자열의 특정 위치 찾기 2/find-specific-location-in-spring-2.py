s = ["apple", "banana", "grape", "blueberry", "orange"]

word = input()
cnt = 0

for i in range(5):
    if (s[i][2] == word) or (s[i][3] == word):
        cnt += 1
        print(s[i])
    
print(cnt)