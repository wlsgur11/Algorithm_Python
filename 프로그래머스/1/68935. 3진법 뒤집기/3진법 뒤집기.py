def trans(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n):
    n = trans(n, 3)
    n = str(n)[::-1]
    n = int(n, 3)
    return n