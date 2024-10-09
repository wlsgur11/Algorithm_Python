import math

def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    ans = []
    front = 0
    for i in range(len(progresses)):
        if progresses[i] > progresses[front]:
            ans.append(i - front)
            front = i
    ans.append(len(progresses) - front)
    return ans