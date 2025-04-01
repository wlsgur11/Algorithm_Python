from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

A = list(permutations(nums, M))
A.sort()

for i in A: print(*i)