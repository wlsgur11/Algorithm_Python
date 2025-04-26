from collections import deque

def solution(numbers, target):    
    cnt = 0

    q = deque([(0, numbers[0]), (0, -numbers[0])])

    while q:
        i, total = q.popleft()

        if total == target and i == len(numbers) - 1:
            cnt += 1

        if i+1 < len(numbers):
            q.append((i+1, total + numbers[i+1]))
            q.append((i+1, total - numbers[i+1]))

    return cnt
        