from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
campus = []
start = []

for i in range(N):
    A = list(sys.stdin.readline().rstrip())
    for j in range(M):
        if A[j] == "I":
            start = [i, j]
    campus.append(A)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
cnt = 0

queue = deque([start])
visited[start[0]][start[1]] = 1

while queue:
    x, y = queue.popleft()
    # print(x, y)
    # print(queue)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if campus[nx][ny] != "X":
                queue.append([nx, ny])
                visited[nx][ny] = 1
                if campus[nx][ny] == "P":
                    cnt += 1

print("TT" if cnt == 0 else cnt)