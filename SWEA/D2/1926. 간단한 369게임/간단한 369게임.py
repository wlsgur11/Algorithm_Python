T = int(input())
ans = []
for i in range(1, T + 1):
    c = str(i)
    count_3 = c.count('3')
    count_6 = c.count('6')
    count_9 = c.count('9')
    
    if count_3 > 0 or count_6 > 0 or count_9 > 0:
        # 3, 6, 9가 포함된 경우
        result = '-' * (count_3 + count_6 + count_9)
        ans.append(result)
    else:
        ans.append(c)

print(*ans)