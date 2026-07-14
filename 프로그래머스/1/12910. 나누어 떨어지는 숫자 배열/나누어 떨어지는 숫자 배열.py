def solution(arr, divisor):
    ans = []
    for num in arr:
        if num % divisor == 0:
            ans.append(num)
    if len(ans) == 0:
        return [-1]
    return sorted(ans)