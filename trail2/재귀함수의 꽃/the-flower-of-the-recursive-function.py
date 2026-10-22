def art_of_func(n):
    if n == 0:
        return
    print(n, end=" ")
    art_of_func(n-1)
    print(n, end=" ")

n = int(input())
art_of_func(n)