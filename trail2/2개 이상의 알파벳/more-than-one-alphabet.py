def is_dif_2word(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] != n[j]:
                return True
    return False

a = input()
print("Yes" if is_dif_2word(a) else "No")