def solution(record):
    ans = []
    names = {}
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            names[i[1]] = i[2]
            ans.append((0, i[1]))
        elif i[0] == "Leave":
            ans.append((1, i[1]))
        elif i[0] == "Change":
            names[i[1]] = i[2]
    
    answer = []
    for j, id in ans:
        if j == 0:
            answer.append(f"{names[id]}님이 들어왔습니다.")
        elif j == 1:
            answer.append(f"{names[id]}님이 나갔습니다.")
    
    return answer