def solution(x):
    A = 0
    for i in str(x):
        A += int(i)
    return x % A == 0