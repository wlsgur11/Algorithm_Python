def hannoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return
        hannoi(n-1, start, via, end)
        answer.append([start, end])
        hannoi(n-1, via, end, start)
        
def solution(n):
    global answer
    answer = []
    hannoi(n, 1, 3, 2)
    return answer