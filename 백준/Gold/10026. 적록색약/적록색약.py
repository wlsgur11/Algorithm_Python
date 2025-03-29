from collections import deque


def bfs(i, j, A, visited):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and A[nx][ny] == A[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny)) 

N = int(input())

change_blind = {'R': 1, 'G': 1, 'B': 2}

RGB = [list(map(str, input())) for _ in range(N)]

blind = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        blind[i][j] = change_blind[RGB[i][j]]

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = [0, 0]

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i, j, RGB, visited1)
            ans[0] += 1
        if not visited2[i][j]:
            bfs(i, j, blind, visited2)
            ans[1] += 1

print(*ans)