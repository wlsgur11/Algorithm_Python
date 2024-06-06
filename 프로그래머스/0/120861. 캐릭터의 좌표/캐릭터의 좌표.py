def solution(keyinput, board):
    ans = [0, 0]
    limit = [[-(board[0]//2), board[0]//2], [-(board[1]//2), board[1]//2]]
    for i in keyinput:
        if i == "left":
            if ans[0] == limit[0][0]: continue
            else: ans[0] -= 1
        if i == "right":
            if ans[0] == limit[0][1]: continue
            else: ans[0] += 1
        if i == "up":
            if ans[1] == limit[1][1]: continue
            else: ans[1] += 1
        if i == "down":
            if ans[1] == limit[1][0]:continue
            else: ans[1] -= 1
    return ans