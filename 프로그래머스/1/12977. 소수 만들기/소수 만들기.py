def solution(nums):
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                count = 1
                A = sum([nums[i], nums[j], nums[k]])
                for num in range(2, A):
                    if A % num == 0:
                        count += 1
                if count == 1:
                    cnt += 1
    return cnt