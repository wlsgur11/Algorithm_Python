import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        if cost > dist[now]:
            continue

        for next_node, weight in graph[now]:
            if dist[next_node] > cost + weight:
                dist[next_node] = cost + weight
                heapq.heappush(heap, (cost + weight, next_node))

    return dist

N, E = map(int, input().split())

graph = [[]for _ in range(N+1)]
distance = [float('inf')] * (N+1)
visited = [False] * (N+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)

route1 = dist1[v1] + distv1[v2] + distv2[N]
route2 = dist1[v2] + distv2[v1] + distv1[N]

result = min(route1, route2)

print(result if result < INF else -1)