from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False       
    return True

def solution(numbers):
    A = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(list(numbers), i):
            A.add(int("".join(j)))
    
    cnt = 0
    for i in A:
        if 2 <= i and isPrime(i):
            cnt += 1
    return cnt