from collections import deque

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def bfs(i):
        q = deque([i])
        visited[i] = True
        
        while q:
            now = q.popleft()
            for j in range(n):
                if computers[now][j] == 1 and not visited[j]:
                    q.append(j)
                    visited[j] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    return cnt