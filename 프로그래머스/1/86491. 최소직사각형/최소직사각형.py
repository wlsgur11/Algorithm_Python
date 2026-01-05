def solution(sizes):
    length, width = 0, 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        if a > length: length = a
        if b > width: width = b
    return length * width