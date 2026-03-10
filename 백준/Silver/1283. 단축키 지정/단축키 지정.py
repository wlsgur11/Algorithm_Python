N = int(input())
op_Set = []

for _ in range(N):
    A = list(input().split())
    is_assigned = False
    
    for i in range(len(A)):
        if A[i][0].upper() not in op_Set:
            op_Set.append(A[i][0].upper())
            A[i] = "[" + A[i][0] + "]" + A[i][1:]
            is_assigned = True
            break
            
    if not is_assigned:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j].upper() not in op_Set:
                    op_Set.append(A[i][j].upper())
                    A[i] = A[i][:j] + "[" + A[i][j] + "]" + A[i][j+1:]
                    is_assigned = True
                    break
            if is_assigned:
                break
                
    print(" ".join(A))