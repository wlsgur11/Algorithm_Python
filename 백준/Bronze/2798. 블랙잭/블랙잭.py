N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            A = nums[i] + nums[j] + nums[k]
            if A <= M and A > ans:
                ans = A
print(ans)