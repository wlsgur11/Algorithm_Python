N, P, Q = map(int, input().split())
A = {0: 1}

def down(i):
    if i in A: return A[i]
    A[i] = down(i//P) + down(i//Q)
    return A[i]

print(down(N))