import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    start, end = map(int, input().split())
    nums.append([start, end])
    
nums = sorted(nums, key=lambda x: (x[1], x[0]))

cnt = 1
i = 1
before = 0

while i < N:
    now = i
    if nums[before][1] <= nums[now][0]:
        cnt += 1
        before = now
    i += 1

print(cnt)