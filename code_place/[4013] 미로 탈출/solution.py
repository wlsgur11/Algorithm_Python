from collections import deque
​
N, K = map(int, input().split())
maps = []
S = [0, 0]
for i in range(N):
    A = list(input())
    maps.append(A)
    if "S" in A:
        S = [i, A.index("S")]
    if "E" in A:
        E = [i, A.index('E')]
​
visited = [[[False] * (K + 1) for _ in range(N)] for _ in range(N)]
​
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
​
q = deque([(S[0], S[1], 0, 0)])
visited[S[0]][S[1]][0] = True
​
found = False
while q:
    x, y, dist, k_count = q.popleft()
    
    if maps[x][y] == 'E':
        print(dist)
        found = True
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
​
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] != 'X':
            nk_count = k_count
            
            if maps[nx][ny] == 'O':
                nk_count += 1
            
            if nk_count <= K and not visited[nx][ny][nk_count]:
                visited[nx][ny][nk_count] = True
                q.append((nx, ny, dist + 1, nk_count))
​
if not found:
    print(-1)