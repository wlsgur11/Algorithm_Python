def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    point1 = 0
    point2 = 0
    point3 = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            point1 += 1
        if answers[i] == b[i%len(b)]:
            point2 += 1
        if answers[i] == c[i%len(c)]:
            point3 += 1
    A = [point1, point2, point3]
    B = []
    C = max(A)
    for i in range(1, len(A)+1):
        if A[i-1] == C:
            B.append(i)
    return B