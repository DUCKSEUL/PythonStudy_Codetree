class bomb:
    def __init__(s, code, color, second):
        s.code = code
        s.color = color
        s.second = second

rcode, rcolor, rs = input().split()
rs = int(rs)

new_bomb = bomb(rcode, rcolor, rs)

print("code :", new_bomb.code)
print("color :", new_bomb.color)
print("second :", new_bomb.second)