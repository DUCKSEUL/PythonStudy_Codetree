def find_max(l):
    if len(l) == 1:
        return l[0]
    min = 101
    for i in range(len(l)):
        if l[i] <= min:
            min = l[i]
            idx = i
    l.pop(idx)
    return find_max(l)

n = int(input())
arr = list(map(int, input().split()))
print(find_max(arr))