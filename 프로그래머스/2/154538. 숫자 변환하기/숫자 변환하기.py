from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    visited = [False] * 1000001
    while q:
        now, cnt = q.popleft()
        if now == y:
            return cnt

        if now + n <= y and not visited[now+n]:
            q.append((now + n, cnt + 1))
            visited[now+n] = True
        if now * 2 <= y and not visited[now*2]:
            q.append((now * 2, cnt + 1))
            visited[now*2] = True
        if now * 3 <= y and not visited[now*3]: 
            q.append((now * 3, cnt + 1))
            visited[now*3] = True
        
    return -1