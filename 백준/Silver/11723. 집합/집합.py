import sys
S = []
M = int(input())
for i in range(M):
    A = sys.stdin.readline().strip()
    if A == 'all': S = [j for j in range(1, 21)]
    elif A == 'empty': S = []
    else:
        command, num = A.split()
        num = int(num)
        if command == 'add':
            if num not in S: S.append(num)
        if command == 'remove':
            if num in S: S.remove(num)
        if command == 'check':
            if num in S: print(1)
            else: print(0)
        if command == 'toggle':
            if num in S: S.remove(num)
            else: S.append(num)