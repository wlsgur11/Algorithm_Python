def solution(order):
    return sum([str(order).count(str(i)) for i in range(3, 10, 3)])