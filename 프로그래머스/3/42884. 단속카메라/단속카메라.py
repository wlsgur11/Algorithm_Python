def solution(routes):
    routes.sort(key=lambda x: x[1])
    ans = 0
    camera = -30001
    
    for route in routes:
        if route[0] > camera:
            camera = route[1]
            ans += 1
    return ans