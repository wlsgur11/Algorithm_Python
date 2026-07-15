def solution(absolutes, signs):
    ans = 0
    for sign, num in zip(signs, absolutes):
        ans += num if sign else -num
    return ans