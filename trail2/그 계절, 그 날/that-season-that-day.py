def is_in_29(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0):
        return True
    return False

def is_in_year(y,m,d):
    if is_in_29(y):
        if m in [4, 6, 9, 11]:
            if d <= 30:
                return True
        elif m == 2:
            if d <= 29:
                return True
        else:
            if d <= 31:
                return True
        return False
    else:
        if m in [4, 6, 9, 11]:
            if d <= 30:
                return True
        elif m == 2:
            if d <= 28:
                return True
        else:
            if d <= 31:
                return True
        return False

def what_season(y,m,d):
    if is_in_year(y,m,d):
        if 3 <= m <= 5:
            return "Spring"
        elif 6 <= m <= 8:
            return "Summer"
        elif 9 <= m <= 11:
            return "Fall"
        else:
            return "Winter"
    else:
        return(-1)
    
y, m, d = map(int, input().split())
print(what_season(y,m,d))