from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in permutations(nums):
            ans.append(i)
        return ans