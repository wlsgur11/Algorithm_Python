def solution(citations):
    A = citations
    A.sort(reverse=True)
    for i in range(len(A)):
        if A[i] < i+1:
            return i
    return len(A)