def solution(n,a,b):
    ans = 0
    while a != b:
        if a % 2 == 1:
            a += 1
        a = a // 2
        if b % 2 == 1:
            b += 1
        b = b // 2
        
        ans += 1
    return ans
            