class member:
    def __init__(self, name=0, score=0):
        self.name = name
        self.score = score

members = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    members.append(member(name, score))
min = 999
for i in range(5):
    if members[i].score <= min:
        min = members[i].score
        idx = i
print(members[idx].name, members[idx].score)