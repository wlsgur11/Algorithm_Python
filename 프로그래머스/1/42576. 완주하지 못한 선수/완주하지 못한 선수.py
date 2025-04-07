def solution(participant, completion):
    p = {}
    for i in participant:
        if i not in p:
            p[i] = 1
        else:
            p[i] += 1
    c = {}
    for i in completion:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    for i in dict(set(p.items()) - set(c.items())).keys():
        return i