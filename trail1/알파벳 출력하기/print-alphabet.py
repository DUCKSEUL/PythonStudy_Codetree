N = int(input())

x = ord('A')

for i in range(N):
    for j in range(N):
        if x == ord('Z') + 1:
            x = ord('A')
        if i >= j:
            print(chr(x), end="")
            x += 1
    print("")