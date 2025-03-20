from collections import deque

N = int(input())
RGB = [list(map(str, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * N for _ in range(N)]

def bfs1(i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and RGB[nx][ny] == RGB[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))

def bfs2(i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if RGB[x][y] != 'B' and RGB[nx][ny] != 'B':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif RGB[x][y] == 'B' and RGB[nx][ny] == 'B':
                    visited[nx][ny] = True
                    q.append((nx, ny))

ans1 = 0
ans2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs1(i, j)
            ans1 += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs2(i, j)
            ans2 += 1

print(ans1, ans2)