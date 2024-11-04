class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                word += i
        word = word.lower()
        if len(word) == 0: return True
        if len(word) % 2 != 0:
            A = word[:len(word) // 2]
            B = word[(len(word)//2)+1:][::-1]
            if A == B: return True
            else: return False
        if len(word) % 2 == 0:
            A = word[:len(word) // 2]
            B = word[(len(word)//2):][::-1]
            if A == B: return True
            else: return False