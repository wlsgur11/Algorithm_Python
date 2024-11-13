from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        A = Counter(s)
        B = Counter(t)
        return (A==B)