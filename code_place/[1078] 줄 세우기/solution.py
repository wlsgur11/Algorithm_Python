N = int(input())
nums = list(map(int, input().split()))
​
dp = [0] * (N+1)
​
for i in nums:
    dp[i] = dp[i-1] + 1
​
print(N - max(dp))