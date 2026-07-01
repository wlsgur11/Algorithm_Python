def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]: ans[0] += 1
        if answers[i] == b[i%len(b)]: ans[1] += 1
        if answers[i] == c[i%len(c)]: ans[2] += 1
    
    maxi = max(ans)
    res = []
    for i in range(1, 4):
        if ans[i-1] == maxi:
            res.append(i)
    return res