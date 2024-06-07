def solution(numbers):
    numbers.sort()
    A = numbers[0] * numbers[1]
    B = numbers[-1] * numbers[-2]
    return max(A, B)