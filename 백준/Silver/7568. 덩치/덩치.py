N = int(input())
arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

rank = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: cnt += 1
    rank.append(cnt+1)
print(*rank)