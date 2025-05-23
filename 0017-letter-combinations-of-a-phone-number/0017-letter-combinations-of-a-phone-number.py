from itertools import permutations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        A = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(combi, next_digits):
            if len(next_digits) == 0:
                ans.append(combi)
            else:
                for i in A[next_digits[0]]:
                    backtrack(combi + i, next_digits[1:])
        
        ans = []
        backtrack("", digits)
        return ans