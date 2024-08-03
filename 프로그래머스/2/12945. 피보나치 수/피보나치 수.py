def solution(n):
    one = 0
    two = 1
    for i in range(2, n+1):
        two, one = one + two, two
    return two % 1234567