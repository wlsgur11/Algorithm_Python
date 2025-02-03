n = int(input())
arr = [1, 2] + ([0] * (n-2))

if n <= 2:
    print(n)
else:
    for i in range(2, n):
        arr[i] = arr[i-2] + arr[i-1]
    print(arr[-1] % 10007)