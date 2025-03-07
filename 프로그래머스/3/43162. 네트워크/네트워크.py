from collections import deque

def solution(n, computers):
    
    def bfs(start):
        q = deque([start])
        visited[start] = True
        
        while q:
            A = q.popleft()
            for neighbor in range(n):
                if computers[A][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
    
    visited = [False] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            ans += 1
    return ans