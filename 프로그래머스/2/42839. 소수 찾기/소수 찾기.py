from itertools import permutations

def solution(numbers):
    ans = []
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))
    new_nums = set([int(("").join(p)) for p in per]) - {0, 1}
    
    cnt = len(new_nums)
    for n in new_nums:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                cnt -= 1
                break
    return cnt
