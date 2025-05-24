for tc in range(1, 11):
    dump = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    for _ in range(dump):
        nums[0], nums[-1] = nums[0] + 1, nums[-1] -1
        nums.sort()
    print(f"#{tc} {max(nums) - min(nums)}")