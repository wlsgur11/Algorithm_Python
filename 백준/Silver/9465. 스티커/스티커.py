T = int(input())
for _ in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * (N+1) for _ in range(2)]
    
    dp[0][1] = nums[0][0]
    dp[1][1] = nums[1][0]

    for j in range(2, N+1):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + nums[0][j-1]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + nums[1][j-1]

    print(max(dp[0][N], dp[1][N]))