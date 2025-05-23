T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_profit = 0
    ans = 0

    for i in range(N-1, -1, -1):
        if nums[i] > max_profit:
            max_profit = nums[i]
        else:
            ans += max_profit - nums[i]

    print(f"#{tc} {ans}")