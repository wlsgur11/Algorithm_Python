def solution(n):
    pre = 0
    cur = 1
    for i in range(2, n+1):
        cur, pre = cur+pre, cur
    return cur % 1234567