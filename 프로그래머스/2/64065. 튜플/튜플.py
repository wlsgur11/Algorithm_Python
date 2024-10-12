def solution(s):
    s = s.replace("{", "")[:-2]
    s = s.split("},")
    if len(s) == 1: return [int(s[0])]
    B = []
    for i in s:
        A = i.split(",")
        B.append(set(A))
    B.sort(key=lambda x: len(x))

    C = list(B[0])
    for i in range(1, len(B)):
        M = B[i] - B[i-1]
        C += list(M)
    ans = []
    for i in C:
        ans.append(int(i))
    return ans