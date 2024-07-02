def solution(arr):
    ans = []
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            continue
        else:
            ans.append(arr[i])
    ans.append(arr[-1])
    return ans