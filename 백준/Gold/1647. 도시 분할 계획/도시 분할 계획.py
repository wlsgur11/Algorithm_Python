import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))


graph.sort()

parent = list(range(n + 1))

ans = 0
last_edge = 0

for c, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        ans += c
        last_edge = c

print(ans - last_edge)