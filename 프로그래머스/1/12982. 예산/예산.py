def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        if budget-i >= 0:
            budget -= i
            cnt += 1
        else:
            break
    return cnt