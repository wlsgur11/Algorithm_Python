from collections import deque

N, M = map(int, input().split())
adj = {i: i for i in range(1, 101)}

for _ in range(N+M):
    a, b = map(int, input().split())
    adj[a] = b

visited = [False] * 101
visited[1] = True
q = deque([(1, 0)])

while q:
    now, step = q.popleft()

    if now == 100:
        print(step)
        break
    
    for i in range(1, 7):
        next = now + i
        if next > 100:
            continue

        next = adj[next]

        if not visited[next]:
            visited[next] = True
            q.append((next, step+1))