def solution(sizes):
    a, b = 0, 0
    for i in range(len(sizes)):
        sizes[i] = [max(sizes[i]), min(sizes[i])]
        if a < sizes[i][0]: a = sizes[i][0]
        if b < sizes[i][1]: b = sizes[i][1]
    return a * b