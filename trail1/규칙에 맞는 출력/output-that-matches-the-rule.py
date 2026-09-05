N = int(input())

for i in range(N, 0, -1):
    for j in range(1, N-i+2):
        print(i+j-1, end=" ")
    print("")