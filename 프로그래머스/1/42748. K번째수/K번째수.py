def solution(array, commands):
    ans = []
    for com in commands:
        ans.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return ans