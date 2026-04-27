import sys
​
N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))
​
low = 1
high = max(times) * M
ans_time = high
​
while low <= high:
    mid = (low + high) // 2
​
    total = sum(mid // t for t in times)
​
    if total >= M:
        ans_time = mid
        high = mid - 1
    else:
        low = mid + 1
​
res = sum((ans_time - 1) // t for t in times)
​
cnt = res
for i in range(N):
    if ans_time % times[i] == 0:
        cnt += 1
        if cnt == M:
            print(f"{i + 1} {ans_time // times[i]}")
            break