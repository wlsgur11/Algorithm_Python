import math

def solution(arr):
    def lcm(a, b):
        return (a*b) // math.gcd(a, b)
    
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans