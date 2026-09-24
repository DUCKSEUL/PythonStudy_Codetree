a, b = tuple(input().split())

num_a, num_b = "", ""

for i in a:
    if ord("0") <= ord(i) <= ord("9"):
        num_a = num_a + i
    else:
        break

for j in b:
    if ord("0") <= ord(j) <= ord("9"):
        num_b = num_b + j
    else:
        break

print(int(num_a) + int(num_b))