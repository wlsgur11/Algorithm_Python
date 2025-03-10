import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dist[i][j] = 0

bfs()

for row in dist:
    print(*row)
