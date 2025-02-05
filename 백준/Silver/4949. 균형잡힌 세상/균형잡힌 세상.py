import sys

while True:
    A = sys.stdin.readline().rstrip()
    if A == ".": break
    stack = []
    for i in A:
        if i in "([": stack.append(i)
        elif i == ")":
            if stack and  stack[-1] == "(": stack.pop()
            else: 
                stack.append(")")
                break
        elif i == "]":
            if stack and stack[-1] == "[": stack.pop()
            else: 
                stack.append("]")
                break
    print("yes" if not stack else "no")