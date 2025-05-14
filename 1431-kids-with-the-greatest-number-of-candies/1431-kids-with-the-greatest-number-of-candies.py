class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        A = max(candies)
        return [A <= i+extraCandies for i in candies]