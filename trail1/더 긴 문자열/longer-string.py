s_arr = list(input().split())

if len(s_arr[0]) > len(s_arr[1]):
    print(s_arr[0], len(s_arr[0]))
elif len(s_arr[0]) == len(s_arr[1]):
    print("same")
else:
    print(s_arr[1], len(s_arr[1]))