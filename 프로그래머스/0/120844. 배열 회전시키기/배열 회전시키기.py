def solution(numbers, direction):
    if direction == "left":
        return [numbers[(i+1)%len(numbers)] for i in range(len(numbers))]
    else:
        return [numbers[(i-1)%len(numbers)] for i in range(len(numbers))]