def fun(k, start):
    if k == M:
        print(*arr)
        return
    
    for i in range(start, N + 1):
        arr[k] = i
        fun(k + 1, i + 1)

N, M = map(int, input().split())
arr = [0] * M
fun(0, 1)
