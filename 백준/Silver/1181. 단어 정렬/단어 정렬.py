N = int(input())

B = set()
for _ in range(N): B.add(input())
A = sorted(list(B))
A.sort(key=len)
for i in A: print(i)