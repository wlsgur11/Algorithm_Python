def solution(n):
    i = 0
    A = bin(n).count('1')
    while True:
        i += 1
        if bin(n+i).count('1') == A:
            return n+i