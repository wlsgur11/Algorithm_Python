def solution(a):
    result = [False for _ in a]
    minfront, minback = float('inf'), float('inf')
    for i in range(len(a)):
        if a[i] < minfront:
            minfront = a[i]
            result[i] = True
        if a[-1-i] < minback:
            minback = a[-1-i]
            result[-1-i] = True
    return sum(result)