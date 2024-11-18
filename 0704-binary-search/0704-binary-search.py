class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high, low = len(nums) - 1, 0

        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1