import sys

N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))
s = [0]
for i in range(N):
    s.append(num_list[i] + s[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(s[j] - s[i-1])