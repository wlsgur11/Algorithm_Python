from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        
        def bfs(a, b):
            q = deque([(a, b)])
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1':
                        q.append((nx, ny))
                        visited[nx][ny] = True



        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1

        return cnt