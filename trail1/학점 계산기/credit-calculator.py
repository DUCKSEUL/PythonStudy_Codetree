N = int(input())

score = list(map(float, input().split()))

sum = 0

for i in score:
    sum += i

avg = sum / N

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")