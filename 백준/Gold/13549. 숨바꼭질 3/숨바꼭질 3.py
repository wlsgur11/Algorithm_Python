from collections import deque

N, K = map(int, input().split())
dist = [float('inf')] * 100001

q = deque([(N)])
dist[N] = 0
while q:
    now = q.popleft()

    if now == K:
        print(dist[now])
        break
    
    if 0 <= now * 2 <= 100000 and dist[now*2] > dist[now]:
        q.appendleft((now*2))
        dist[now*2] = dist[now]
    if 0 <= now + 1 <= 100000 and dist[now+1] > dist[now] + 1:
        q.append((now+1))
        dist[now+1] = dist[now] + 1
    if 0 <= now - 1 <= 100000 and dist[now-1] > dist[now] + 1:
        q.append((now-1))
        dist[now-1] = dist[now] + 1