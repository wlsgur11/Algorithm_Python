from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)
    print(graph)
    stack = ["ICN"]
    route = []
    
    while stack:
        while graph[stack[-1]]:
            A = graph[stack[-1]].pop()
            stack.append(A)
        route.append(stack.pop())
    return route[::-1]