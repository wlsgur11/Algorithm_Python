T = int(input())
for i in range(T):
    ans = []
    num_list = list(map(int, input().split()))
    print("#" + str(i+1), end=" ")
    for j in num_list:
        if j % 2 != 0:
            ans.append(j)
    print(sum(ans))