import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:    
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if 0 <= ni < N and 0 <= nj < N and nums[ni][nj] == '1' and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
        
    return cnt

N = int(input())
nums = [input().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
res = []

for i in range(N):
    for j in range(N):
        if nums[i][j] == '1' and not visited[i][j]:
            res.append(bfs(i, j)) 

res.sort()
print(len(res))
for i in res: print(i)