N = int(input())
num = list(map(int, input().split()))
nums = sorted(list(set(num)))

dic = {nums[i]: i for i in range(len(nums))}

for i in num:
    print(dic[i], end=" ")