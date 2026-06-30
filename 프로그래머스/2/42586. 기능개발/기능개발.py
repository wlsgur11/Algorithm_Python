import math

def solution(progresses, speeds):
    stack = []
    
    for i, j in zip(progresses, speeds):
        stack.append(math.ceil((100-i) / j))
        
    if len(stack) == 1:
        return stack
    
    ans = []
    cur = stack[0]
    cnt = 1
    
    for i in range(1, len(stack)):
        if stack[i] <= cur:
            cnt += 1
        else:
            ans.append(cnt)
            cur = stack[i]
            cnt = 1
    ans.append(cnt)
    return ans
    