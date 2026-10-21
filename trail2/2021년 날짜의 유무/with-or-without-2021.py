def is_in_2021(m,d):
    if m == 2:
        if d <= 28:
            return "Yes"
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d <= 31:
            return "Yes"
    elif m >= 13:
        return "No"
    else:
        if d <= 30:
            return "Yes"
    return "No"

m, d = map(int, input().split())
print(is_in_2021(m,d))