A = input()
B = input()
la = len(A)
N = 0

while True:
    if N >= la:
        break
    if A == B:
        break
    else:
        N += 1
        A = A[-1] + A[:-1]

if N == la:
    print(-1)
else:
    print(N)