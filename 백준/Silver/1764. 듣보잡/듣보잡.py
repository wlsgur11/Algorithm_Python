N, M = map(int, input().split())
set1 = set()
set2 = set()

for i in range(N): set1.add(input())
for i in range(M): set2.add(input())

lst = list(set1 & set2)
lst.sort()
print(len(lst))
for i in lst: print(i)