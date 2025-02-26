from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        A = queue.popleft()
        if A == K:
            return visited[K]
        for i in (A-1, A+1, A*2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[A] + 1
                queue.append(i)
        
N, K = map(int, input().split())
visited = [0] * 100001
print(bfs(N))