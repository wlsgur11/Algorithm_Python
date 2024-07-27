def solution(n):
    ans = 1
    for i in range(1, n//2 + 1):
        cnt = 0
        while cnt < n:
            cnt  += i
            if cnt == n:
                ans += 1
                break
            i += 1
    return ans