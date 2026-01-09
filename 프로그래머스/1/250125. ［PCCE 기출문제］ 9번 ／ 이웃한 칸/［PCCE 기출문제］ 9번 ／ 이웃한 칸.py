def solution(board, h, w):
    cnt = 0
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and board[h][w] == board[nx][ny]:
            cnt += 1
    return cnt