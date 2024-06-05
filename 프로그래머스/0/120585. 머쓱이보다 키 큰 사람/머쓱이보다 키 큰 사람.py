def solution(array, height):
    array.append(height)
    A = sorted(array, reverse=True)
    return A.index(height)