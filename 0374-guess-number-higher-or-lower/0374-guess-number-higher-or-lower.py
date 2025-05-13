class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            A = guess(mid)
            if A == -1:
                high = mid
            elif A == 1:
                low = mid + 1
            else:
                return mid