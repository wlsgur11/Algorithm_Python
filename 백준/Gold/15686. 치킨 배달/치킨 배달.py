from itertools import combinations

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

ans = 1e9
for comb in combinations(chicken, M):
    total = 0
    for h in house:
        min_dist = 1e9
        for c in comb:
            min_dist = min(min_dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        total += min_dist
    ans = min(ans, total)
print(ans)