import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

A = sorted(list(set(permutations(nums, M))))

for i in A:
    print(*i)