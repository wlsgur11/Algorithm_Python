N = int(input())
nums = list(map(int, input().split()))
M = int(input())
​
low = 0
high = max(nums)
result = 0
​
while low <= high:
    mid = (low + high) // 2
    res = 0
​
    for i in range(N):
        if nums[i] > mid:
            res += mid
        else:
            res += nums[i]
​
    if res <= M:
        result = mid
        low = mid + 1
​
    else:
        high = mid - 1
​
print(result)