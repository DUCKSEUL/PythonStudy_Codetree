N = int(input())

for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if i < j:
            print(" ", end=" ")
        else:
            print(j, end=" ")
    print("")