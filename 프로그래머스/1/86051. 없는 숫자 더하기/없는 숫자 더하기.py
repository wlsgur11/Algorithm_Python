def solution(numbers):
    a = [i for i in range(10)]
    b = []
    for i in range(10):
        if a[i] not in numbers:
            b.append(a[i])
    return sum(b)