N = int(input())
M = int(input())
S = input()

IOI = 'I' + 'OI' * N
length, cnt = len(IOI), 0

for i in range(M - length + 1):
    A = S[i:i+length]
    if A == IOI: cnt += 1
print(cnt)