import math
​
N = int(input())
stations = list(map(int, input().split()))
dist = int(input())
​
ans = 0
cur_pos = 1
range_size = dist * 2 + 1
​
for station in stations:
    if cur_pos < station - dist:
        blank = (station - dist) - cur_pos
        ans += math.ceil(blank / range_size)
    
    cur_pos = station + dist + 1
if cur_pos <= N:
    blank = N - cur_pos + 1
    ans += math.ceil(blank/range_size)
​
print(ans)