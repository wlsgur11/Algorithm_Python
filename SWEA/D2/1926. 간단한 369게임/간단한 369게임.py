N = int(input())
ans = []

for i in range(1, N+1):
    num = str(i)

    cnt_3 = num.count('3')
    cnt_6 = num.count('6')
    cnt_9 = num.count('9')

    if cnt_3 > 0 or cnt_6 > 0 or cnt_9 > 0:
        ans.append('-' * (cnt_3 + cnt_6 + cnt_9))
    else: ans.append(i)

print(*ans)