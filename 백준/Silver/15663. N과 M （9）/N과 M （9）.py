import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
res = list()
visited = [False] * n

def bt(depth):
    if depth == m:
        print(*res)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != nums[i]:
            prev = nums[i]
            visited[i] = True
            res.append(prev)
            bt(depth + 1)
            visited[i] = False
            res.pop()

bt(0)