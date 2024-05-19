def solution(n):
    dp = factorial(10)
    for i in range(1, 11):
        if n >= dp[i]:
            ans = i
    return ans
def factorial(n):
    dp = [1] + [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = i * dp[i-1]
    return dp