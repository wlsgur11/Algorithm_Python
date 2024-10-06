def solution(clothes):
    A = {}
    for i, j in clothes:
        if j not in A:
            A[j] = [i]
        else:
            A[j] += [i]
    ans = 1
    for _, i in A.items():
        ans *= (len(i) + 1)
    return ans - 1