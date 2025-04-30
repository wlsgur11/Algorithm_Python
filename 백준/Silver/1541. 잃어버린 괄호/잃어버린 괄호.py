A = input()
parts = A.split('-')

sums = []
for part in parts:
    numbers = map(int, part.split('+'))
    sums.append(sum(numbers))

res = sums[0]
for i in sums[1:]: res -= i
print(res)