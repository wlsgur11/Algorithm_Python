def solution(elements):
    res = set()
    
    length = len(elements)
    elements = elements * 2
    for i in range(length):
        for j in range(length):
            res.add(sum(elements[j:j+i+1]))
    return len(res)