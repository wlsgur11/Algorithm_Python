import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())

boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

days = -1
total_tomato = 0
q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 1:
                q.append((h, i, j, 0))
            elif boxes[h][i][j] == 0:
                total_tomato += 1

while q:
    z, x, y, day = q.popleft()
    days  = max(day, days)

    for d in range(6):
        nz, nx, ny = z + dz[d], x + dx[d], y + dy[d]

        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and boxes[nz][nx][ny] == 0:
            boxes[nz][nx][ny] = 1
            q.append((nz, nx, ny, day + 1))
            total_tomato -= 1


if total_tomato > 0:
    print(-1)
else:
    print(days)