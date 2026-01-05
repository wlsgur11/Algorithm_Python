def solution(d, budget):
    d.sort()
    ans = 0
    for i in d:
        if budget - i < 0:
            break
        else:
            budget -= i
            ans += 1
    return ans