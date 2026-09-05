N = int(input())

for i in range(1,N+1):
    for j in range(1,N+1):
        if N-i+1 >= j:
            print(f"{i} * {j} = {i*j}", end=" ")
        if N-i >= j:
            print("/", end=" ")
    print("")