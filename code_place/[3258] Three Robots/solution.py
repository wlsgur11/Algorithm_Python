import sys
import heapq
​
def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    queue = [(0, start)]
​
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
​
        if dist[curr_node] < curr_dist:
            continue
​
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return dist
​
input = sys.stdin.readline
​
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
​
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
​
u, v, w = map(int, input().split())
​
dist_u = dijkstra(u)
dist_v = dijkstra(v)
dist_w = dijkstra(w)
​
min_time = float('inf')
​
for i in range(1, N+1):
    max_time = max(dist_u[i], dist_v[i], dist_w[i])
​
    if max_time < min_time:
        min_time = max_time
        
print(min_time)