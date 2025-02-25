import sys
input = sys.stdin.readline
from collections import deque

def bfs(adj_list, start):
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in adj_list[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    adj_list[B].append(A)

res = []
for i in range(1, N+1):
    res.append(bfs(adj_list, i))
        
print(res.index(min(res))+1)