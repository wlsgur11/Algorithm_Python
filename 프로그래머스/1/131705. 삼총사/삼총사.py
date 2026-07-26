from itertools import combinations

def solution(number):
    ans = 0
    for j in combinations(number, 3):
        if sum(j) == 0:
            ans += 1
    return ans