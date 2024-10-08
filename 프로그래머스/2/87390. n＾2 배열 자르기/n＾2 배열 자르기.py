def solution(n, left, right):
    result = []
    
    for i in range(left, right + 1):
        A = (i // n) + 1
        j = i % n
        result.append(max(A, j + 1))
    
    return result