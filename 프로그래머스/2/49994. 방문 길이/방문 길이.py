def solution(dirs):
    sets = set()
    udirl = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    x, y = 0, 0
    
    for d in dirs:
        dx, dy = udirl[d]
        ny = y + dy
        nx = x + dx
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            sets.add(((x, y), (nx, ny)))
            sets.add(((nx, ny), (x, y)))
            y = ny
            x = nx
    return len(sets) // 2