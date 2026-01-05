def solution(sizes):
    l, w = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > l: l = sizes[i][0]
        if sizes[i][1] > w: w = sizes[i][1]
    return l*w