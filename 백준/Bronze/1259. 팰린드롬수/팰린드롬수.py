import sys

while True:
    A = sys.stdin.readline().strip()
    if A == '0': break
    if A == A[::-1]: print('yes')
    else: print('no')