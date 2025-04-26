from collections import deque

def solution(numbers, target):
    global cnt
    cnt = 0
    
    def bfs(numbers, target):
        global cnt
        q = deque([(0, numbers[0]), (0, -numbers[0])])
        
        while q:
            i, total = q.popleft()
            
            if total == target and i == len(numbers) - 1:
                cnt += 1
            if i+1 < len(numbers):
                q.append((i+1, total + numbers[i+1]))
                q.append((i+1, total - numbers[i+1]))
    
    bfs(numbers, target)
    return cnt
        