N, K = map(int, input().split())
up = 1
down = 1
for i in range(1, K+1):
    up = up * N
    N -= 1
    down = down * i
print(up // down)
