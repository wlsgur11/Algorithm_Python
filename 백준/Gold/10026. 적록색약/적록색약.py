from collections import deque


def bfs(i, j, A):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and A[nx][ny] == A[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny)) 

N = int(input())

change_normal = {'R': 1, 'G': 2, 'B': 3}
change_blind = {'R': 1, 'G': 1, 'B': 2}

first = [list(map(str, input())) for _ in range(N)]

normal = [[0] * N for _ in range(N)]
blind = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        normal[i][j] = change_normal[first[i][j]]
        blind[i][j] = change_blind[first[i][j]]

visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = [0, 0]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, normal)
            ans[0] += 1

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, blind)
            ans[1] += 1

print(*ans)