s = input()

cnt1, cnt2 = "No", "No"

for i in range(len(s)-1):
    if (s[i] + s[i+1] == "ee"):
        cnt1 = "Yes"
    elif (s[i] + s[i+1] == "ab"):
        cnt2 = "Yes"

print(cnt1, cnt2)