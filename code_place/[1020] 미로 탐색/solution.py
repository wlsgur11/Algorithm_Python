from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[0][0] = True
q = deque([(0, 0, 1)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, dist = q.popleft()
    if x == N - 1 and y == M - 1:
        print(dist)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny, dist + 1))