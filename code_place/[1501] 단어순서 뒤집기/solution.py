A = int(input())
for i in range(1, A+1):
    B = list(map(str, input().split()))
    print(f"Case #{i}: {" ".join(B[::-1])}")