def find_max_reward(arr, k):
    memo = {}
    
    def dfs(arr, k):
        arr_str = ''.join(arr)
        
        if (arr_str, k) in memo:
            return memo[(arr_str, k)]
        
        if k == 0:
            return int(arr_str)
        
        max_val = 0
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                max_val = max(max_val, dfs(arr, k-1))
                arr[i], arr[j] = arr[j], arr[i]
        
        memo[(arr_str, k)] = max_val
        return max_val
    
    return dfs(arr, k)

def has_duplicate(arr):
    return len(arr) != len(set(arr))

T = int(input())
for t in range(1, T + 1):
    num, k = input().split()
    arr = list(num)
    k = int(k)

    k = min(k, len(arr) * len(arr))
    
    result = find_max_reward(arr, k)
    print(f"#{t} {result}")