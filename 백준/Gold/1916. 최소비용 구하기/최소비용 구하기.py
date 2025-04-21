import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())

distance = [float('inf')] * (N+1)
distance[start] = 0

heap = []
heapq.heappush(heap, (0, start))

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue

    for next, cost in graph[now]:
        new_cost = dist + cost
        if new_cost < distance[next]:
            distance[next] = new_cost
            heapq.heappush(heap, (new_cost, next))

print(distance[end])