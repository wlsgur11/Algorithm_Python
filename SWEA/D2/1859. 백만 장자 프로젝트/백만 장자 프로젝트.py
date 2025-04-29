T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_price = 0
    profit = 0

    for i in range(N-1, -1, -1):
        if nums[i] > max_price:
            max_price = nums[i]
        else:
            profit += max_price - nums[i]
    print(f"#{t+1} {profit}")