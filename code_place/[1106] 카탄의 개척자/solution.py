import sys
​
input = sys.stdin.readline
MAX_N = 10000
board = [0] * (MAX_N + 1)
resource_counts = [0] * 6
​
def precompute():
    board[1] = 1
    resource_counts[1] += 1
    
    grid = {(0, 0): 1}
    dirs = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
    
    moves = []
    k = 1
    while len(moves) < MAX_N:
        moves.append(0)
        moves.extend([1] * (k - 1))
        moves.extend([2] * k)
        moves.extend([3] * k)
        moves.extend([4] * k)
        moves.extend([5] * k)
        moves.extend([0] * k)
        k += 1
        
    q, r = 0, 0
    
    for i in range(2, MAX_N + 1):
        move = moves[i - 2]
        dq, dr = dirs[move]
        q += dq
        r += dr
​
        used = set()
        for ndq, ndr in dirs:
            nq, nr = q + ndq, r + ndr
            if (nq, nr) in grid:
                used.add(grid[(nq, nr)])
        
        selected_resource = 0
        best_count = float('inf')
        
        for res in range(1, 6):
            if res not in used:
                if resource_counts[res] < best_count:
                    best_count = resource_counts[res]
                    selected_resource = res
​
        grid[(q, r)] = selected_resource
        board[i] = selected_resource
        resource_counts[selected_resource] += 1
​
precompute()
​
c = int(input().strip())
​
for _ in range(c):
    n = int(input().strip())
    print(board[n])