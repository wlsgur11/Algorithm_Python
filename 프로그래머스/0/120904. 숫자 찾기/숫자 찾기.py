def solution(num, k):
    num = str(num)
    ans = -1
    for i in range(len(num)):
        if num[i] == str(k):
            ans = i+1
            return ans
    return ans