N = int(input())
romans = [1, 5, 10, 50]
res = set()

def S(cnt, total, start_index):
    if cnt == N:
        res.add(total)
        return

    for i in range(start_index, 4):
        S(cnt + 1, total + romans[i], i)

S(0, 0, 0)
print(len(res))