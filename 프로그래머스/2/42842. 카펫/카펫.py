def solution(brown, yellow):
    num = []
    ans = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            num.append(i)
    for i in range(len(num)-1):
        for j in range(i, len(num)):
            if num[i] * num[j] == (brown + yellow):
                ans.append([num[i], num[j]])
    for i in range(len(ans)):
        if ((ans[i][0] - 2) * (ans[i][1] - 2) == yellow):
            return ans[i][::-1]

#(w-2)*(h-2) = brown 을 만족시켜야 해당 w, h 리턴값.