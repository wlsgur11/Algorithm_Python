def solution(numlist, n):
    numlist.sort(reverse=True)
    A = {}
    for i in numlist:
        A[i] = abs(i-n)
    B = sorted(A.items(), key = lambda x: x[1])
    ans = []
    for i, _ in B:
        ans.append(i)
    return ans