n = int(input())
arr = list(map(int, input().split()))

new_arr = []

for i in arr:
    new_arr.append(i)
    if len(new_arr) % 2 != 0:
        new_arr.sort()
        print(new_arr[(len(new_arr)-1)//2], end=" ")