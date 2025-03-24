from collections import deque

N, M = map(int, input().split())
adj = {i: i for i in range(1, 101)}  # 기본적으로 자기 자신을 가리키도록 초기화

for _ in range(N + M):
    x, y = map(int, input().split())
    adj[x] = y  # 사다리와 뱀 적용

q = deque([(1, 0)])  # 1번 칸에서 시작
visited = [False] * 101
visited[1] = True  # 시작 지점 방문 처리

while q:
    pos, step = q.popleft()

    if pos == 100:  # 100번 칸 도착하면 종료
        print(step)
        break

    for i in range(1, 7):  # 주사위 1~6까지 던지기
        next_pos = pos + i
        if next_pos > 100:
            continue

        next_pos = adj[next_pos]  # 사다리나 뱀 적용

        if not visited[next_pos]:  # 방문하지 않은 경우만 이동
            visited[next_pos] = True
            q.append((next_pos, step + 1))
