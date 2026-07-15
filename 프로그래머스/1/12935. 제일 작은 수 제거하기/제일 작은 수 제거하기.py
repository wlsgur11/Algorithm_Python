def solution(arr):
    del arr[arr.index(min(arr))]
    if arr:
        return arr
    return [-1]
    