def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            parent[b_root] = a_root
            return True
        return False
    
    total = 0
    for a, b, cost in costs:
        if union(a, b):
            total += cost
    return total