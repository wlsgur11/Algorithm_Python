def solution(N, stages):
    A = {}
    B = {}
    for i in range(N+1):
        A[i+1] = 0
        B[i+1] = 0
    for i in range(len(stages)):
        A[stages[i]] += 1
    C = sum(A.values())
    for i in range(N+1):
        if A[i+1] <= 0 or C <= 0:
            B[i+1] = 0
        else:
            B[i+1] = A[i+1] / C
        C -= A[i+1]
    del B[N+1]
    ans = sorted(B.items(), key = lambda x: x[1], reverse=True)
    res = []
    for i, _ in ans:
        res.append(i)
    return res