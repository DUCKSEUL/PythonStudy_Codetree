n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)] == b:
        print("Yes")
        cnt += 1
        break

if cnt == 0:
    print("No")