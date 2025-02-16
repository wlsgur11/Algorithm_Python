K, N = map(int, input().split())
num = [int(input()) for _ in range(K)]
start, end = 1, max(num)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in num: cnt += i // mid
    if cnt >= N: start = mid + 1
    else: end = mid - 1
print(end)