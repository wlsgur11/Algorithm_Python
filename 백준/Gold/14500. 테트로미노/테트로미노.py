N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

tetromino = [
    # ㅡ 모양
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],

    # 정사각형 모양
    [(0,0), (0,1), (1,0), (1,1)],

    # L 모양 (8가지 회전)
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (1,0), (2,0), (0,1)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (0,2), (1,2)],

    # 번개 모양 (S, Z)
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (0,1), (1,1), (1,2)],

    # ㅗ 모양 (4가지)
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,1), (1,0), (1,1), (2,1)],
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (1,1), (2,0)]
]

ans = 0

for i in range(N):
    for j in range(M):
        for shape in tetromino:
            total = 0
            valid = True
            for dx, dy in shape:
                x, y = i + dx, j + dy
                if 0 <= x < N and 0 <= y < M:
                    total += arr[x][y]
                else:
                    valid = False
                    break
            if valid:
                ans = max(ans, total)
print(ans)