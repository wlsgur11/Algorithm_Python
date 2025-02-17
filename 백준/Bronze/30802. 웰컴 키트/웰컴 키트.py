import math
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0
for i in size: cnt += math.ceil(i/T)
print(cnt)
print(N // P, N % P)