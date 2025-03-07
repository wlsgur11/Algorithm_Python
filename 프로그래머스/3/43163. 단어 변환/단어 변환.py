from collections import deque

def check(w1, w2):
    cnt = 0
    for a, b in zip(w1, w2):
        if a != b: 
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        cur, step = q.popleft()
        
        if cur == target:
            return step
        
        for word in words:
            if word not in visited and check(cur, word):
                visited.add(word)
                q.append((word, step+1))
    return 0