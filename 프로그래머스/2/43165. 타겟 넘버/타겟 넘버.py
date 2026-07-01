def solution(numbers, target):    
    global cnt
    cnt = 0
    n = len(numbers)
    
    def dfs(i, total):
        global cnt
        if i == n:
            if total == target:
                cnt += 1
            return
        else:
            dfs(i+1, total - numbers[i])
            dfs(i+1, total + numbers[i])
    dfs(0, 0)
    return cnt