N, M = map(int, input().split())

A = set(input() for _ in range(N))
B = set(input() for _ in range(M))

C = list(A.intersection(B))
print(len(C))
C.sort()
for i in C: print(i)