from collections import deque

def solution(priorities, location):
    ans = []
    queue = deque([(o, p) for o, p in zip(range(len(priorities)), priorities)])
    answer = queue[location]
    arr = sorted(priorities[:], reverse=True)
    i = 0
    while len(queue):
        if arr[i] == queue[0][1]:
            ans.append(queue.popleft())
            i += 1
        else:
            queue.append(queue.popleft())
    for i in range(len(ans)):
        if ans[i] == answer:
            return i+1