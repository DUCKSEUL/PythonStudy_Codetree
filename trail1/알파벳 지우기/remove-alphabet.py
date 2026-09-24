s1 = input()
s2 = input()

s1_num, s2_num = "", ""

for i in s1:
    if ord("0") <= ord(i) <= ord("9"):
        s1_num = s1_num + i

for j in s2:
    if ord("0") <= ord(j) <= ord("9"):
        s2_num = s2_num + j

print(int(s1_num) + int(s2_num))