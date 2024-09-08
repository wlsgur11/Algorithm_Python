from itertools import permutations

def solution(k, dungeons):
    res = []
    for i in permutations(dungeons, len(dungeons)):
        least = k
        temp = 0
        for j in range(len(dungeons)):
            if i[j][0] <= least:
                least -= i[j][1]
                temp += 1
            else:
                continue
        res.append(temp)
    return max(res)