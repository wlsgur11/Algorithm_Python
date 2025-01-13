# 풀이법1. 3중 for문 : 100개의 카드가 있으니까 O(N^3)해도 괜찮을 듯 하다.
# 풀이법2. dfs는 잘 모르겠다.
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0

for i in range(len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for k in range(j+1, len(num_list)):
            now = num_list[i] + num_list[j] + num_list[k]
            if (ans < now) and (now <= M):
                ans = now
print(ans)
