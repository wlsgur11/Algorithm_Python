N = int(input())
stack = []
point = 0
​
for _ in range(N):
    A = list(map(int, input().split()))
    if A[0] == 1:
        stack.append(A)
    if stack:
        stack[-1][2] -= 1
        if stack[-1][2] == 0:
            point += stack.pop()[1]
​
print(point)