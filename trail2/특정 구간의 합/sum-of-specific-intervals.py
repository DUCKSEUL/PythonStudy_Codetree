n, m = map(int, input().split())
a = list(map(int, input().split()))

def sum_a_part(q1, q2):
    sum = 0
    for i in range(q1-1, q2):
        sum += a[i]
    return sum

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum_a_part(a1, a2))