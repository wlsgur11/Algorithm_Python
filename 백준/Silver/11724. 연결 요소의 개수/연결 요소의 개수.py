import sys

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def make_closed_list(nums, graph):
    for A, B in nums:
        graph[A].append(B)
        graph[B].append(A)
    return graph

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
closed_list = make_closed_list(nums, graph)

visited, cnt = [0] * (N + 1), 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        else:
            dfs(i)
            cnt += 1
print(cnt)