def solution(spell, dic):
    for i in dic:
        time = []
        for j in spell:
            if i.count(j) == 1:
                time.append(i.count(j))
        if len(spell) == len(time):
            return 1
    return 2