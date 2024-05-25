def solution(my_string):
    ans = ''
    for i in my_string:
        if i.islower(): ans += i.upper()
        else: ans += i.lower()
    return ans