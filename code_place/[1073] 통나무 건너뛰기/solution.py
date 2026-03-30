N = int(input())
​
for _ in range(N):
    A = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    maxi = 0
    for i in range(A):
        B = max(abs(nums[i] - nums[max(0, i-2)]), abs(nums[i] - nums[min(A-1, i+2)]))
        if maxi < B:
            maxi = B
​
    print(maxi)