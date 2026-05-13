                if grid[nr][nc] > 0 and not visited[nr][nc]:
for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            icebergs.append((i, j))
​
years = 0
while icebergs:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    temp_icebergs = []
    
    for r, c in icebergs:
        if grid[r][c] > 0 and not visited[r][c]:
            cnt += 1
            if cnt >= 2: break
            bfs(r, c, visited, grid, N, M)
    
    if cnt >= 2:
        print(years)
        sys.exit()
    
    melt_list = []
    for r, c in icebergs:
        sea = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == 0:
                sea += 1
        melt_list.append((r, c, sea))
    
    next_icebergs = []
    for r, c, sea in melt_list:
        grid[r][c] = max(0, grid[r][c] - sea)
        if grid[r][c] > 0:
            next_icebergs.append((r, c))
    
    icebergs = next_icebergs
    years += 1
​
print(0)