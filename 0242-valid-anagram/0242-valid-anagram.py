from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A = Counter(s)
        B = Counter(t)
        return (A==B)