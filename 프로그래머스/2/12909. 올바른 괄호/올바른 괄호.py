def solution(s):
    A = 0
    for i in s:
        if i == "(":
            A += 1
        elif i == ")":
            A -= 1
        if A < 0:
            return False
    if A == 0:
        return True
    else:
        return False