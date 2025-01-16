def gcd(A, B):
    while (B != 0): A, B = B, A % B
    return A

A, B = map(int, input().split())
print(gcd(A, B))
print((A * B) // gcd(A, B))