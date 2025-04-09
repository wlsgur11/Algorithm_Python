import math

def solution(progresses, speeds):
    arr = [math.ceil((100-a) / b) for a, b in zip(progresses, speeds)]
    ans = []
    front = 0
    print(arr)
    for i in range(len(arr)):
        if arr[i] > arr[front]:
            ans.append(i-front)
            front = i
    ans.append(len(arr) - front)
    return ans