def solution(s):
    cnt = 0
    for i in range(len(s)):
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif (stack[-1] == '(' and c == ')') or \
                (stack[-1] == '{' and c == '}') or \
                (stack[-1] == '[' and c == ']'):
                    stack.pop()
            else:
                stack.append(c)
        if not stack:
            cnt += 1
        s = s[1:] + s[0]
                    
    return cnt