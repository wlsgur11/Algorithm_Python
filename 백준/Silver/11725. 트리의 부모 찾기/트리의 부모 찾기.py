from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

parent = [0] * (N+1)

q = deque([1])
while q:
    node = q.popleft()
    for i in adj[node]:
        if parent[i] == 0:
            parent[i] = node
            q.append(i)

for i in range(2, N+1):
    print(parent[i])