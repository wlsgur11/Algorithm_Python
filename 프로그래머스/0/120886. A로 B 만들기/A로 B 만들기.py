def solution(before, after):
    A = sorted(list(before))
    B = sorted(list(after))
    if A == B: return 1
    return 0