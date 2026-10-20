def calc(a, c, b):
    if c == "+":
        return int(a) + int(b)
    elif c == "-":
        return int(a) - int(b)
    elif c == "/":
        return int(a) // int(b)
    elif c == "*":
        return int(a) * int(b)
    else:
        return "NA"

arr = list(input().split())
ans = calc(arr[0], arr[1], arr[2])

if ans == "NA":
    print("False")
else:
    print(f"{arr[0]} {arr[1]} {arr[2]} = {ans}")