def solution(X, Y):
    x_cnt = {str(i): X.count(str(i)) for i in range(10)}
    y_cnt = {str(i): Y.count(str(i)) for i in range(10)}
    
    res = []
    
    for i in range(9, -1, -1):
        digit = str(i)
        count = min(x_cnt[digit], y_cnt[digit])
        res.append(digit * count)
    
    answer = "".join(res)
    
    if not answer: 
        return "-1"
    if answer[0] == "0":
        return "0"
        
    return answer