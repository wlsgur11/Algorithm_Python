숫자들 = list(map(int, input().split()))
if len(숫자들) == 1:
    print(-1)
else:
    숫자들.remove(min(숫자들))
    print(*숫자들)
​