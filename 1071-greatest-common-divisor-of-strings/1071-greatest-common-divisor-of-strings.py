class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        A, B = len(str1), len(str2)
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        res = gcd(A, B)
        candidate = str1[:res]

        if str1 == candidate * (A // res) and str2 == candidate * (B // res):
            return candidate
        else:
            return ""