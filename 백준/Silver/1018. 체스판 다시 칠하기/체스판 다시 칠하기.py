import sys

M, N = map(int, input().split())
board = []
cnt = []
for i in range(M):
    board.append(sys.stdin.readline().strip())

for i in range(M-7):
    for j in range(N-7):
        W = 0
        B = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0:
                    if board[a][b] == 'B': W += 1
                    else: B += 1
                else:
                    if board[a][b] == 'B': B += 1
                    else: W += 1
        cnt.append(W)
        cnt.append(B)
print(min(cnt))