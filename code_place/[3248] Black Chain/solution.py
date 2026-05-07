엔 = int(input())
k = 1
while True:
    max_n = (k + 1) * (1 << (k + 1)) - 1
​
    if max_n >= 엔:
        print(k)
        break
    k += 1