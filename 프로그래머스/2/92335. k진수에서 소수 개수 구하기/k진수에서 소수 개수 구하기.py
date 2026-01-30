def solution(n, k):
    def isPrime(num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    res = ''
    while n > 0:
        res += str(n%k)
        n = n // k
    
    ans = 0
    A = " ".join(res[::-1].split('0')).split()
    for i in A:
        if isPrime(int(i)):
            ans += 1
        
    return ans