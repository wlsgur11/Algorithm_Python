def solution(rsp):
    A = {'0': '5', '2': '0', '5': '2'}
    return "".join(A[i] for i in rsp)