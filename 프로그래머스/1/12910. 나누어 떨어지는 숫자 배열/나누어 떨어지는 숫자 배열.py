def solution(arr, divisor):
    ans = []
    for i in arr:
        if i % divisor == 0:
            ans.append(i)
    if len(ans) == 0:
        ans.append(-1)
    return sorted(ans)