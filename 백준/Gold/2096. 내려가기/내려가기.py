import sys
input = sys.stdin.readline

N = int(input())

a, b, c = map(int, input().split())
dp_max = [a, b, c]
dp_min = [a, b, c]

for _ in range(N-1):
    a, b, c = map(int, input().split())

    max0 = max(dp_max[0], dp_max[1]) + a
    max1 = max(dp_max[0], dp_max[1], dp_max[2]) + b
    max2 = max(dp_max[1], dp_max[2]) + c

    min0 = min(dp_min[0], dp_min[1]) + a
    min1 = min(dp_min[0], dp_min[1], dp_min[2]) + b
    min2 = min(dp_min[1], dp_min[2]) + c

    dp_max = [max0, max1, max2]
    dp_min = [min0, min1, min2]

print(max(dp_max), min(dp_min))