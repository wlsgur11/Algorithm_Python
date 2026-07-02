from collections import Counter
from math import comb

def solution(weights):
    cnt = Counter(w * 4 for w in weights)
    ans = 0
    for w, c in cnt.items():
        ans += comb(c, 2)
        for ratio in (w*2, w*3//2, w*4//3):
            if ratio in cnt and ratio != w:
                ans += c * cnt[ratio]
    return ans