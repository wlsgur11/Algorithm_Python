def solution(ingredient):
    cnt = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        while len(stack) > 3:
            if stack[-4:] == [1, 2, 3, 1]:
                cnt += 1
                for _ in range(4):
                    stack.pop()
            else: break
    return cnt