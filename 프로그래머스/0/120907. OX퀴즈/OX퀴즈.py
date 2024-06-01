def solution(quiz):
    ans = []
    for i in range(len(quiz)):
        A = ''
        for j in quiz[i]:
            if j == " ":
                continue
            if j == "=":
                A += "=="
            else:
                A += j
        if eval(A):
            ans.append("O")
        else:
            ans.append("X")
    return ans