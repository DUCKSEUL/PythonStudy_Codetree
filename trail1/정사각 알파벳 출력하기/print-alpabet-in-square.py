N = int(input())

str = ord('A')

for i in range(N):
    for j in range(N):
        print(chr(str), end="")
        str += 1
    print("")