s = input()
cnt1, cnt2 = 0, 0

for i in range(len(s)-1):
    if (s[i] + s[i+1]) == "ee":
        cnt1 += 1
    elif (s[i] + s[i+1]) == "eb":
        cnt2 += 1
        
print(cnt1, cnt2)