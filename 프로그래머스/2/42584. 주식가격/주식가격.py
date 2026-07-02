from collections import deque

def solution(prices):
    q = deque(prices)
    ans = []
    
    while q:
        n = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if n > i:
                break
        ans.append(sec)
    return ans 