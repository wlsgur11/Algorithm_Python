def solution(rsp):
    ans = ''
    for i in rsp:
        if i == '0': ans += '5'
        if i == '2': ans += '0'
        if i == '5': ans += '2'
    return ans