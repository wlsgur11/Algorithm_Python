def solution(participant, completion):
    p = {}
    for i in participant:
        if i not in p:
            p[i] = 1
        else:
            p[i] += 1
    for i in completion:
        p[i] -= 1
        if p[i] == 0:
            del p[i]
    for i in p.keys():
        return i