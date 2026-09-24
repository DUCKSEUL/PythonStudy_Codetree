A = input()

sum = 0

for i in A:
    if (ord("0") <= ord(i) <= ord("9")):
        sum += int(i)

print(sum)