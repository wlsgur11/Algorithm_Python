N, M = map(int, input().split())
nums = list(map(int, input().split()))
​
​
cnt, right = 0, 0
cur_sum = 0
​
for left in range(N):
    while cur_sum< M and right < N:
        cur_sum += nums[right]
        right += 1
    
    if cur_sum == M:
        cnt += 1
​
    cur_sum -= nums[left]
​
print(cnt)