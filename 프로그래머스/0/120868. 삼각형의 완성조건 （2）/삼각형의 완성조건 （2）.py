def solution(sides):
    cnt = 0
    for i in range(1, sum(sides)):
        if i <= max(sides):
            if min(sides) + i > max(sides):
                cnt += 1
        else:
            if sum(sides) > i:
                cnt += 1
    return cnt