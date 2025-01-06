def solution(n, t, m, p):
    time = t*m
    num = ''
    for i in range(time):
        num += convert(i, n)
    ans = ''
    for i in range(p-1, len(num), m):
        ans += num[i]
    return ans[:t].upper()

def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]