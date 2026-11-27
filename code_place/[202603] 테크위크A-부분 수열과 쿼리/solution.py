T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort(reverse=True)
    print(sum(nums[:K]))