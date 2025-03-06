import sys
input = sys.stdin.readline

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

for i in range(N): # 경유할 노드
    for j in range(N): # 출발 노드
        for k in range(N): # 도착 노드
            if adj[j][i] and adj[i][k]:
                adj[j][k] = 1

for row in adj: 
    print(*row)