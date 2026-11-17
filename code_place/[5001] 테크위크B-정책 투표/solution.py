from collections import Counter

A = int(input())
B = input().split()

cnt = Counter(B)
if cnt.most_common()[0][1] >= (A//2)+1:
    print(cnt.most_common()[0][0])
else:
    print(-1)