def solution(s):
    s = s.split(" ")
    a = []
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                a.append(i[j].upper())
            else:
                a.append(i[j].lower())
        a.append(" ")
    return "".join(a)[:-1]