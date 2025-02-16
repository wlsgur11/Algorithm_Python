import sys, heapq
q = []
N = int(input())
for i in range(N):
    A = int(sys.stdin.readline())
    if A > 0: heapq.heappush(q, A)
    else:
        if len(q) > 0: print(heapq.heappop(q))
        else: print(0)