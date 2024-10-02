from collections import Counter

def solution(want, number, discount):
    ans = 0
    di = {}
    
    for w, n in zip(want, number):
        di[w] = n
        
    for i in range(len(discount) - 9):
        c = Counter(discount[i:i+10])
        if c == di:
            ans += 1
    return ans