import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    entry = {}
    k = int(input())

    for _ in range(k):
        A, B = input().split()
        B = int(B)

        if A == "I":
            heapq.heappush(min_heap, B)
            heapq.heappush(max_heap, -B)
            entry[B] = entry.get(B, 0) + 1
        elif A == "D":
            if B == -1:
                while min_heap and entry[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    val = heapq.heappop(min_heap)
                    entry[val] -= 1
            elif B == 1:
                while max_heap and entry[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    val = -heapq.heappop(max_heap)
                    entry[val] -= 1
    
    while min_heap and entry[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")