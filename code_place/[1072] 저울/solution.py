A = int(input())
nums = list(map(int, input().split()))

nums.sort()

cur = 0
for i in range(A):
    if nums[i] <= cur + 1:
        cur += nums[i]
print(cur + 1)