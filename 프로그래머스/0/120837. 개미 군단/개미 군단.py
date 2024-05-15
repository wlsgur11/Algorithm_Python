def solution(hp):
    ans = 0
    for i in range(5, 0, -2):
        ans += hp // i
        hp %= i
    return ans
        