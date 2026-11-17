import sys
from collections import deque

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
targets = list(map(int, data[2:2 + m]))

dq = deque(range(1, n + 1))
answer = 0

for t in targets:
    idx = dq.index(t)
    if idx <= len(dq) - idx:
        dq.rotate(-idx)
        answer += idx
    else:
        dq.rotate(len(dq) - idx)
        answer += len(dq) - idx
    dq.popleft()

print(answer)