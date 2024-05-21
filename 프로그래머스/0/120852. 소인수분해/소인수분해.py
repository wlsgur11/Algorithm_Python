def solution(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            if i not in factors:
                factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors