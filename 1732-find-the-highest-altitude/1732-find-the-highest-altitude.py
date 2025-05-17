class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        A = [0 for _ in range(len(gain) + 1)]
        for i in range(1, len(gain) + 1):
            A[i] = A[i-1] + gain[i-1]
        return max(A)