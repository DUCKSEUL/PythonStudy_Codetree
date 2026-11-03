class personal:
    def __init__(s, name, code, loc):
        s.name = name
        s.code = code
        s.loc = loc
    
    def print_per(s):
        print("name", s.name)
        print("addr", s.code)
        print("city", s.loc)

arr = []
arr_name = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    arr.append(personal(a, b, c))
    arr_name.append(a)

arr_name.sort()
for i in range(n):
    if arr[i].name == arr_name[n-1]:
        arr[i].print_per()
