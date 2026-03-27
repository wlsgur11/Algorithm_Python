N = int(input())
​
for _ in range(N):
    M = int(input())
    A = bin(M)[2:]
    res = ""
    for i in A:
        if i == "0":
            res += '1'
        else:
            res += '0'
    res = "0b" + res[::-1]
    print(int(res, 2))