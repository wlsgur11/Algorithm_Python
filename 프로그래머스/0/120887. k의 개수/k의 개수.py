def solution(i, j, k):
    A = ''
    for a in range(i, j+1):
        A += str(a)
    return A.count(str(k))