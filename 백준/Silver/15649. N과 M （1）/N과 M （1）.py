def fun(k):
    if k == M:
        print(*arr)
        return    
    
    for i in range(1, N+1):
        if not issued[i]:
            arr[k] = i
            issued[i] = 1
            fun(k+1)
            issued[i] = 0

N, M = map(int, input().split())
arr = [0] * M
issued = [0] * (N+1)
fun(0)