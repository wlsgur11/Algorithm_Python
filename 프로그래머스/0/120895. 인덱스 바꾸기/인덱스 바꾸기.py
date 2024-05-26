def solution(my_string, num1, num2):
    A = list(my_string)
    A[num1], A[num2] = A[num2], A[num1]
    return "".join(A)