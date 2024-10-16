from collections import Counter
def solution(topping):
    ans = 0
    A = Counter(topping)
    B = set()
    
    for i in topping:
        A[i] -= 1
        B.add(i)
        
        if A[i] == 0:
            A.pop(i)
        if len(A) == len(B):
            ans += 1
    return ans