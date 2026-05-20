import sys, random
input = sys.stdin.readline
flag = -1
n = int(input())
arr = list(map(int, input().split()))
for i in range(15):
    r = random.randint(0, n - 1)
    if arr.count(arr[r]) > n // 2:
        flag = arr[r]
        break
print(flag)