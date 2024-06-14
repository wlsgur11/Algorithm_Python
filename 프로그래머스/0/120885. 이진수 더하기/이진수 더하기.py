def solution(bin1, bin2):
    A = int("0b"+bin1, 2) + int("0b"+bin2, 2)
    return bin(A).replace("0b", "")