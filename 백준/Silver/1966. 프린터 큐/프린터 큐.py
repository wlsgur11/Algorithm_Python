T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    result = 1
    while data:
        if data[0] < max(data):
            data.append(data.pop(0))
        else:
            if M == 0:
                break

            data.pop(0)
            result += 1
            
        if M > 0: M = M - 1 
        else: M = len(data) - 1
    print(result)