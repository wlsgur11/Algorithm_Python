n = int(input())
A = n * 5
for _ in range(n):
    print("@" * A)
for _ in range(n * 3):
    print("@" * n)
for _ in range(n):
    print("@" * A)