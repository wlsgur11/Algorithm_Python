from collections import deque

N, M = map(int, input().split())
adj = {i: i for i in range(1, 101)}

for _ in range(N+M):
    x, y = map(int, input().split())
    adj[x] = y

q = deque([(1, 0)])
visited = [False] * 101
visited[1] = True
while q:
    pos, step = q.popleft()

    if pos == 100:
        print(step)
        break

    for i in range(1, 7):
        next = pos + i
        if next > 100:
            continue

        next = adj[next]

        if not visited[next]:
            visited[next] = True
            q.append((next, step+1))