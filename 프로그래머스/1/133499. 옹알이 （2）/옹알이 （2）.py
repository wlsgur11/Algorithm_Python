def solution(babbling):
    result = 0
    A = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        for j in range(len(A)):
            babbling[i] = babbling[i].replace(A[j], str(j))
        if babbling[i].isdigit():
            result += 1
            for k in range(len(babbling[i]) - 1):
                if babbling[i][k] == babbling[i][k+1]:
                    result -= 1
                    break
    return result