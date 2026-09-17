A = input()
com = input()

for i in range(len(com)):
    if com[i] == 'L':
        A = A[1:] + A[0]
    elif com[i] == 'R':
        A = A[-1] + A[:-1]

print(A)