def solution(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = int(s[i])
    A = ''
    A += str(min(s)) + " "
    A += str(max(s))
    return A