def solution(arr):
    A = 1
    for i in arr:
        A *= i
    for i in range(2, A+1):
        cnt = 0
        for j in arr:
            if i % j == 0: cnt += 1
        if cnt == len(arr): return i
    return A