def solution(n, w, num):
    if (n / w) + 0.5 > n//w:
        A = n//w + 1
    else:
        A = n//w
    palette = [[0] * w for _ in range(A)]
    
    for i in range(n):
        palette[i//w][i%w] = i+1
        
    for i in range(A):
        if i % 2 != 0:
            palette[i].reverse()
    
    for i in range(A):
        for j in range(w):
            if palette[i][j] == num:
                x = i
                y = j
    
    cnt = 0
    for i in range(A):
        now = palette.pop()
        if now[y] >= num:
            cnt += 1
    return cnt