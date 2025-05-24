T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort(reverse=True)
    
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(f"#{tc} {dic[0][0]}")