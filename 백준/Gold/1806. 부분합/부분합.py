import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
cur = 0
ans = N+1

while True:
    if cur >= S:
        ans = min(ans, end - start)
        cur -= nums[start]
        start += 1
    elif end == N:
        break
    else:
        cur += nums[end]
        end += 1
print(ans if ans != N+1 else 0)