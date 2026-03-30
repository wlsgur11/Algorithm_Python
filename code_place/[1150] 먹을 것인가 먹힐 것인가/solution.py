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
        left, right, temp = 0, M - 1, 0
        while left <= right:
            mid = (left + right) // 2
​
            if B[mid] < a_val:
                temp = mid + 1
                left = mid + 1
            else:
                right = mid - 1
​
        cnt += temp
    print(cnt)