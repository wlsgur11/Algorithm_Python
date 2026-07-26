from itertools import combinations

def solution(numbers):
    ans = set()
    for i in combinations(numbers, 2):
        ans.add(sum(i))
    return sorted(ans)