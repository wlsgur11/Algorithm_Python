def solution(numbers):
    ans = [-1 for i in range(len(numbers))]

    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            ans[idx] = numbers[i]
            
        stack.append(i)
    return ans