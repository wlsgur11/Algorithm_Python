def solution(numbers):
    ans = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            if a in ans:
                continue
            else:
                ans.append(a) 
    return sorted(ans)