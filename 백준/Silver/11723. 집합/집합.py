import sys
S = 0
M = int(input())
for i in range(M):
    A = sys.stdin.readline().strip()
    if A == 'all': S = (1 << 21) - 1
    elif A == 'empty': S = 0
    else:
        command, num = A.split()
        num = int(num)
        if command == 'add': S |= (1 << num)
        if command == 'remove': S &= ~(1 << num)
        if command == 'check': print(1 if S & (1 << num) != 0 else 0)
        if command == 'toggle': S ^= (1 << num)