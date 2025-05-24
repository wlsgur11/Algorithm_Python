T = int(input())

for tc in range(1, T+1):
    N = int(input())

    nums = [[0] * N for _ in range(N)]

    x, y = 0, 0
    direction = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(1, N*N+1):
        nums[x][y] = i

        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or nums[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny

    print(f"#{tc}")
    for row in nums:
        print(*row)