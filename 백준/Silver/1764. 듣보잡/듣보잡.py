N, M = map(int, input().split())
dict = {}
for i in range(N+M):
    name = input()
    if name not in dict: dict[name] = 1
    else: dict[name] += 1
ans = []
for i in dict:
    if dict[i] == 2: ans.append(i)
print(len(ans))
ans.sort()
for i in ans: print(i)