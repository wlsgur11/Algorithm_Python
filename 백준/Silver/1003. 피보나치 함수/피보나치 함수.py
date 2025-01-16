import sys

dp = [[1, 0], [0, 1]]

def fibo(N):
    if  N < len(dp):
        return
    if N > 1 and N >= len(dp):
        for i in range(len(dp), N+1):
            dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    ans = fibo(N)
    print(*dp[N])