dp = [0, 1, 2, 4] + [0] * 8
for i in range(4, 12):
    for j in range(i-3,i):
        dp[i] += dp[j]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])