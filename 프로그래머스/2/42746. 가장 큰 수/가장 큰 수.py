def solution(numbers):
    nums = [str(i) for i in numbers]
    nums.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(nums)))