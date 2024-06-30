def solution(price, money, count):
    ans = sum([price * i for i in range(1, count + 1)]) - money
    if ans < 0:
        return 0
    else:
        return ans