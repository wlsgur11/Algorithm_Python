import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0 
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new)
        ans += 1
        
    return ans