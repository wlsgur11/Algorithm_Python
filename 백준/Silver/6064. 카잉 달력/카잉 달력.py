import sys, math
input = sys.stdin.readline

def calc(M, N, x, y):
    lcm = (M * N) // math.gcd(M, N)  # 최소공배수(LCM)
    
    i = x  # x에서 시작하여 M씩 증가
    while i <= lcm:
        if (i - 1) % N + 1 == y:  # x는 이미 만족하므로 y만 확인
            return i
        i += M  # M씩 증가하면서 확인

    return -1  # 조건을 만족하는 해가 없을 경우

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(calc(M, N, x, y))
