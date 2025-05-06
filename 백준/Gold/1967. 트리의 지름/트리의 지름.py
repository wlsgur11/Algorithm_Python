import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, dist):
    for next_node, weight in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = dist + weight
            dfs(next_node, dist + weight)

visited = [-1] * (N + 1)
visited[1] = 0
dfs(1, 0)

max_node = visited.index(max(visited))

visited = [-1] * (N + 1)
visited[max_node] = 0
dfs(max_node, 0)

print(max(visited))