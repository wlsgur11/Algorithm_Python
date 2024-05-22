def solution(s):
    ans = 0
    s = s.split()
    for i in range(len(s)):
        if s[i] == 'Z':
            ans -= int(s[i-1])
        else:
            ans += int(s[i])
    return ans