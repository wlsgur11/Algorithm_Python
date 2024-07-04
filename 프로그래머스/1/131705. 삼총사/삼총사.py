import itertools

def solution(number):
    cnt = 0
    for i in itertools.combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt