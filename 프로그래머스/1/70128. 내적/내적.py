def solution(a, b):
    ans = []
    for i in range(len(a)):
        ans.append(a[i] * b[i])
    return sum(ans)