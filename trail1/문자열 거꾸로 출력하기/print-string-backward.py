while True:
    s = input()
    if s == "END":
        break
    for i in range(len(s)):
        print(s[len(s)-1-i], end="")
    print("")