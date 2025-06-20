from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in set(permutations(nums, M)):
    print(*i)