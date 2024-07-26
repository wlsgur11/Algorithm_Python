def solution(s):
    A = 0
    cnt = 0
    while(True):
        cnt += 1
        A += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        if s == "1":
            break
    return [cnt, A]