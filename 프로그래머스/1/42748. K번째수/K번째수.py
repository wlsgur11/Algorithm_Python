def solution(array, commands):
    ans = []
    for i in range(len(commands)):
        if commands[i][0] == commands[i][1]:
            ans.append(array[commands[i][0]-1])
        else:
            ans.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return ans