import sys
input = sys.stdin.readline

def check(nums, C, mid):
    cnt = 1
    last = nums[0]

    for i in range(1, N):
        if nums[i] - last >= mid:
            cnt += 1
            last = nums[i]

            if cnt >= C:
                return True
    return False

N, C = map(int, input().split())

nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()
low, high = 1, nums[-1] - nums[0]

while low <= high:
    mid = (low + high) // 2

    if check(nums, C, mid):
        best = mid
        low = mid + 1
    else:
        high = mid - 1

print(best)