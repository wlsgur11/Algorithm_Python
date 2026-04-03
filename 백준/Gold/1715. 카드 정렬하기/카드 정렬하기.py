import heapq

N = int(input())
q = []
ans = 0

for _ in range(N):
    heapq.heappush(q, int(input()))

while len(q) > 1:
    A = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, A)
    ans += A

print(ans)