from collections import deque

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    q = deque([(x, y)])
    union = [(x, y)]
    people = country[x][y]
    visited[x][y] = True


    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(country[cx][cy] - country[nx][ny]) <= R:
                    q.append((nx, ny))
                    union.append((nx, ny))
                    people += country[nx][ny]
                    visited[nx][ny] = True
    if len(union) > 1:
        new_population = people // len(union)
        for ux, uy in union:
            country[ux][uy] = new_population
        return True
    return False

days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)
