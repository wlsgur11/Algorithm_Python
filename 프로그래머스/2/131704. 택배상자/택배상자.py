def solution(order):
    ans = 0
    stack = []
    for i in range(1, len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[ans]:
            stack.pop()
            ans += 1
            
    return ans