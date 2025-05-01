N, M = map(int, input().split())
truth = list(map(int, input().split()))
truth = truth[1:]

parent = [i for i in range(N + 1)]
party = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

for _ in range(M):
    P = list(map(int, input().split()))
    P = P[1:]
    for i in range(len(P) - 1):
        union(P[i], P[i+1])
    party.append(P)

root_t = set(find(t) for t in truth)

res = 0
for p in party:
    if all(find(i) not in root_t for i in p):
        res += 1
print(res)