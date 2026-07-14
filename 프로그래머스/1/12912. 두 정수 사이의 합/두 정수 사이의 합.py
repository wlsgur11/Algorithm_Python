def solution(a, b):
    ans = 0
    for i in range(min(a, b) ,max(a, b)+1):
        ans += i
    return ans