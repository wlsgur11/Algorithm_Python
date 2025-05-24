from collections import deque

def bfs(graph):
    N = len(graph)
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0
    q = deque([(0, 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        
        if x == N-1 and y == N-1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_time = visited[x][y] + graph[nx][ny]
                if new_time < visited[nx][ny]:
                    visited[nx][ny] = new_time
                    q.append((nx, ny))
                
    return visited[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    print(f"#{tc} {bfs(graph)}")
