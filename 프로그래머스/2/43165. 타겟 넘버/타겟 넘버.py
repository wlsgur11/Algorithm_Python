def solution(numbers, target):
    global ans
    ans = 0
    def dfs(i, total):
        global ans
        if (i == len(numbers)):
            if total == target:
                ans += 1
            return
        dfs(i+1, total + numbers[i])
        dfs(i+1, total - numbers[i])
        return
    dfs(0, 0)
    return ans