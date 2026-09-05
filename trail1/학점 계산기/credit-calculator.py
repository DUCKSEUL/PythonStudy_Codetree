N = int(input())

score = list(map(float, input().split()))

sum = sum(score)
avg = sum / N

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")