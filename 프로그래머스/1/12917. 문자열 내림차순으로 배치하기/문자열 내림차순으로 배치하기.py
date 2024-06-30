def solution(s):
    A = [ord(i) for i in s]
    return "".join([chr(i) for i in sorted(A, reverse=True)])