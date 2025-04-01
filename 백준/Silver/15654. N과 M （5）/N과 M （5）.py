from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

A = list(permutations(nums, M))

for i in A: print(*i)