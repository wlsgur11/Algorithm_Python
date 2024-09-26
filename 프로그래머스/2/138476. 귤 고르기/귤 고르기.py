def solution(k, tangerine):
    di = {}
    ans = 0
    
    for i in tangerine: 
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    
    
    di = dict(sorted(di.items(), key=lambda x: x[1], reverse=True))
    
    for i in di:
        if k <= 0:
            return ans
        k -= di[i]
        ans += 1
    return ans