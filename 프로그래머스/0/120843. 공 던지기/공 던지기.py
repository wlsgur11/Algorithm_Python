def solution(numbers, k):
    return [numbers[i%len(numbers)] for i in range(0, 2*k, 2)][-1]