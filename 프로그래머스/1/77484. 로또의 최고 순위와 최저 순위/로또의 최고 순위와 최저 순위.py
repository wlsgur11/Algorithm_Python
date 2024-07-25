def solution(lottos, win_nums):
    A = {}
    ans = []
    zero = 0
    for i in range(len(win_nums)):
        A[win_nums[i]] = win_nums[i] in lottos
        if lottos[i] == 0:
            zero += 1
    low = sum(A.values())
    high = low + zero
    if high == 0:
        ans.append(6)
    else:
        ans.append(7-high)
    if low == 0:
        ans.append(6)
    else:
        ans.append(7 - low)
    return ans