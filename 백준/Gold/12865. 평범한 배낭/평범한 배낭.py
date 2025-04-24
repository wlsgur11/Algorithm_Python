N, K = map(int, input().split())

stuff = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    stuff.append((W, V))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < stuff[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuff[i][0]] + stuff[i][1])
print(dp[N][K])