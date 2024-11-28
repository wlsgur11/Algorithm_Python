n = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(n):
    a, b = map(int, input().split())
    for j in range(b, b + 10):
        for k in range(a, a+10):
            arr[j][k] = 1

res = 0
for i in arr:
    res += sum(i)
print(res)