from collections import deque

def bfs(A, B):
    q = deque([(A, '')])
    visited = [False] * 10000
    visited[A] = True

    while q:
        now, ans = q.popleft()

        if now == B:
            return ans

        D = (2 * now) % 10000
        if not visited[D]:
            visited[D] = True
            q.append((D, ans + 'D'))

        S = (now - 1) % 10000
        if not visited[S]:
            visited[S] = True
            q.append((S, ans + 'S'))

        L = (now % 1000) * 10 + (now // 1000)
        if not visited[L]:
            visited[L] = True
            q.append((L, ans + 'L'))

        R = (now % 10) * 1000 + (now // 10)
        if not visited[R]:
            visited[R] = True
            q.append((R, ans + 'R'))

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
