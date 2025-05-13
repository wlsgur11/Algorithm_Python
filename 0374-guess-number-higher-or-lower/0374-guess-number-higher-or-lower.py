# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        mid = (low + high) // 2
        while guess(mid) != 0:
            if guess(mid) == -1:
                high = mid
            elif guess(mid) == 1:
                low = mid + 1
            mid = (low + high) // 2
        return mid