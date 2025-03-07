from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, dist = q.popleft()
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append((nx, ny, dist+1))
                visited[nx][ny] = True
    return -1