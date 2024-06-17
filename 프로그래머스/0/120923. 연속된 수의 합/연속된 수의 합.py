def solution(num, total):
    for i in range(-100, 1000 - num):
        a = []
        for j in range(i, i + num):
            a.append(j)
        if sum(a) == total:
            return a