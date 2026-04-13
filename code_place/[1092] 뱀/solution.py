import sys
from collections import deque
​
input = sys.stdin.read().split()
N = int(input[0])
K = int(input[1])
​
board = [[0] * (N + 1) for _ in range(N + 1)]
​
idx = 2
for _ in range(K):
    r, c = int(input[idx]), int(input[idx+1])
    board[r][c] = 1
    idx += 2
​
L = int(input[idx])
idx += 1
times = {}
for _ in range(L):
    x = int(input[idx])
    c = input[idx+1]
    times[x] = c
    idx += 2
​
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
​
direction = 1
time = 0
x, y = 1, 1
snake = deque([(x, y)])
board[x][y] = 2
​
while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
​
    if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
        if board[nx][ny] == 0:
            tx, ty = snake.popleft()
            board[tx][ty] = 0
        
        board[nx][ny] = 2
        snake.append((nx, ny))
        x, y = nx, ny
        
        if time in times:
            if times[time] == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
    else:
        break
        
print(time)