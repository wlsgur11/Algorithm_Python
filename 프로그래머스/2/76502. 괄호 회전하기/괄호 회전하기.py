def solution(s):
    cnt = 0
    for i in range(len(s)):
        x = (s+s[:i])[i:]
        
        stack = []
        for j in x:
            if stack:
                if j == ")" and stack[-1] == "(":
                    stack.pop()
                elif j == "}" and stack[-1] == "{":
                    stack.pop()
                elif j == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(j)
            else:
                stack.append(j)
        if len(stack) == 0:
            cnt += 1
    return cnt