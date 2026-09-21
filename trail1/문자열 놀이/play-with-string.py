s = tuple(input().split())

ss = s[0]
len_Q = int(s[1])

ques = []
for _ in range(len_Q):
    ques.append(input().split())

for i in range(len_Q):
    ss = list(ss)
    if ques[i][0] == "1":
        ques[i][1], ques[i][2] = int(ques[i][1]), int(ques[i][2])
        ss[ques[i][1]-1], ss[ques[i][2]-1] = ss[ques[i][2]-1], ss[ques[i][1]-1]
        ss = ''.join(ss)
        print(ss)
    elif ques[i][0] == "2":
        new_s = []
        for j in range(len(ss)):
            if ss[j] == ques[i][1]:
                new_s.append(ques[i][2])
            else:
                new_s.append(ss[j])
        new_s = ''.join(new_s)
        print(new_s)
        ss = new_s