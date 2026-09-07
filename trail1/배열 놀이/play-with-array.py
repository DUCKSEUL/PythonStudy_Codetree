arr = list(map(int, input().split()))
arr_num = list(map(int, input().split()))

for _ in range(arr[1]):
    quest = list(map(int, input().split()))
    if quest[0] == 1:
        print(arr_num[quest[1]-1], end="")
    elif quest[0] == 2:
        idx = -1
        for i, char in enumerate(arr_num):
            if char == quest[1]:
                idx = i
                break
        if idx == -1:
            print("0", end="")
        else:
            print(idx+1, end="")
    elif quest[0] == 3:
        for j in range(quest[1], quest[2]+1):
            print(arr_num[j-1], end=" ")
    print("")