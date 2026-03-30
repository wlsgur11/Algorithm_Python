from bisect import bisect_left
​
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0
​
    for a_val in A:
        cnt += bisect_left(B, a_val)
    print(cnt)