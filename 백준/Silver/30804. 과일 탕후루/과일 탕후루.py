import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

left = 0
cnt = {}
maximum = 0

for right in range(N):
    current = nums[right]
    if current in cnt:
        cnt[current] += 1
    else:
        cnt[current] = 1

    while len(cnt) > 2:
        remove = nums[left]
        cnt[remove] -= 1

        if cnt[remove] == 0:
            del cnt[remove]
        
        left += 1
    maximum = max(maximum, right - left + 1)
print(maximum)