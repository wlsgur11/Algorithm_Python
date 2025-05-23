for tc in range(1, 11):
    length = int(input())
    nums = list(map(int, input().split()))
    ans = 0

    for i in range(2, length-2):
        sec = max(nums[i-2:i] + nums[i+1:i+3])
        if nums[i] - sec >= 0:
            ans += nums[i] - sec
    print(f"#{tc} {ans}")