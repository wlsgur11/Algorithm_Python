def solution(name, yearning, photo):
    A = {}
    for i in range(len(name)):
        A[name[i]] = yearning[i]
    
    ans = []
    for i in photo:
        B = 0
        for s in i:
            if s in name:
                B += A[s]
        ans.append(B)
    return ans