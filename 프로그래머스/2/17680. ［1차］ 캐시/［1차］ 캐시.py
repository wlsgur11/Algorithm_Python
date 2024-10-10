from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    cities = [i.lower() for i in cities]
    cnt = 0
    for i in cities:
        if cacheSize == 0:
            return 5 * len(cities)
        if i in cache:
            cache.remove(i)
            cache.append(i)
            cnt += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(i)
                cnt += 5
            else:
                cache.append(i)
                cnt += 5
    return cnt