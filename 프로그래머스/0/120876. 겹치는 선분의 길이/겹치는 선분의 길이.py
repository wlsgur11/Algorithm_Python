def solution(lines):
    dp = [0]* 201
    cnt = 0
    for line in lines:
        A, B = line
        A += 100
        B += 100
        for i in range(B-A):
            dp[A+i] +=1
    for i in range(201):
        if dp[i] > 1:
            cnt += 1
    return cnt