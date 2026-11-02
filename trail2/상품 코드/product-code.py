class product:
    def __init__(s, name="codetree", code=50):
        s.name = name
        s.code = code
    
    def print(s):
        print("product", s.code, "is", s.name)

nn, nc = input().split()
nc = int(nc)

p1 = product()
p1.print()
p1.name = nn
p1.code = nc
p1.print()