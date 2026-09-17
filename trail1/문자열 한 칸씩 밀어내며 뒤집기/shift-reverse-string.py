arr = list(input().split())
s, nQ = arr[0], int(arr[1])

for _ in range(nQ):
    Q = int(input())
    if Q == 1:
        s = s[1:] + s[0]
    elif Q == 2:
        s = s[-1] + s[:-1] 
    elif Q == 3:
        s = s[-1:-len(s)-1:-1]

    print(s)
