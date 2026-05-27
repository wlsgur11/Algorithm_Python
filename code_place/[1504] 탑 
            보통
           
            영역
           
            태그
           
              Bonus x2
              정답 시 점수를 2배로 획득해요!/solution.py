import sys
​
input = sys.stdin.readline
​
N = int(input())
heights = list(map(int, input().split()))
​
stack = []
answer = []
​
for i in range(N):
​
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
​
    if stack:
        answer.append(stack[-1][0])
    else:
        answer.append(0)
​
    stack.append((i + 1, heights[i]))
​
print(*answer)