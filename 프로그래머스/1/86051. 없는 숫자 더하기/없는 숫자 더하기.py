def solution(numbers):
    num = set(numbers)
    nums = set([i for i in range(10)])
    return sum(nums - num)