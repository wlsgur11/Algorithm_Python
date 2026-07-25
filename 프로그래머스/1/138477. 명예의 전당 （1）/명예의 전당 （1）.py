import heapq

def solution(k, score):
    h = []
    ans = []
    for i in score:
        heapq.heappush(h, i)
        if len(h) > k:
            heapq.heappop(h)
        ans.append(h[0])
    return ans