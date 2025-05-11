T = int(input())

for t in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    direction = 0
    
    for num in range(1, N*N + 1):
        snail[x][y] = num
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x, y = nx, ny
    
    print(f"#{t}")
    for row in snail:
        print(*row)