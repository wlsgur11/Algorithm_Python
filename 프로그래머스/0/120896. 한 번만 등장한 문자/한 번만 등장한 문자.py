def solution(s):
    a = {}
    b = ''
    for i in sorted(list(set(s))):
        if s.count(i) == 1: a[i] = s.count(i)
    for i in a.keys(): b += i
    return b