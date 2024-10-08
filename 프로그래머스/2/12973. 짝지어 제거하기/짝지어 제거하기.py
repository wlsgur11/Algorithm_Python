def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        return 1
    return 0