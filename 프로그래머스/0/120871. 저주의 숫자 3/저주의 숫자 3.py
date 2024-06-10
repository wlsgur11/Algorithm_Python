def solution(n):
    A = 0
    for i in range(n):
        A += 1
        while A % 3 == 0 or "3" in str(A):
            A += 1
    return A