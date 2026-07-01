from collections import deque

def solution(maps):
    q = deque([(0, 0, 1)])
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while q:
        x, y, total = q.popleft()
        
        if x == n-1 and y == m-1:
            return total
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and nx < n and 0 <= ny and ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append((nx, ny, total+1))
                visited[nx][ny] = True
        
    return -1