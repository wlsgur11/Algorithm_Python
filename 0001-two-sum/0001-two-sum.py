class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {nums[0]: target - nums[0]}
        for i in range(1, len(nums)):
            dic[nums[i]] = target - nums[i]
            if target - nums[i] in dic.keys():
                one = nums.index(target - nums[i])
                if one == i:
                    continue
                return [one, i]