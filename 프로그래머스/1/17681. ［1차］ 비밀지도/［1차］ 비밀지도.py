def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        a = int(bin(arr1[i])[2:], 2)
        b = int(bin(arr2[i])[2:], 2)
        c = bin(a|b)[2:]
        temp = ''
        if len(c) != n:
            c = ("0" * (n-len(c))) + c
        for j in c:
            if j == "0":
                temp += " "
            else:
                temp += "#"
        ans.append(temp)
    return ans