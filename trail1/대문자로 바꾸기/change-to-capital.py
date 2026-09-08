#print(ord('A'))
#print(ord('a'))

arr = []

for _ in range(5):
    arr.append(list(input().split()))

for i in range(5):
    for j in range(3):
        print(chr(ord(arr[i][j])-32), end=" ")
    print("")