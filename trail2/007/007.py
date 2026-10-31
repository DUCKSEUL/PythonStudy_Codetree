class secret_007:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

secret_code, meeting_point, time = input().split()
time = int(time)

haha = secret_007(secret_code, meeting_point, time)

print("secret code :", haha.code)
print("meeting point :", haha.point)
print("time :", haha.time)