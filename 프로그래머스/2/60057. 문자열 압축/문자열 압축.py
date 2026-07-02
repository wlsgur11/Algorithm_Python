def solution(s):
    ans = len(s)
    for size in range(1, len(s) // 2 + 1):
        comp = ""
        prev = s[:size]
        count = 1
        for j in range(size, len(s), size):
            cur = s[j:j+size]
            if prev == cur:
                count += 1
            else:
                comp += (str(count) if count > 1 else "") + prev
                prev = cur
                count = 1
        comp += (str(count) if count > 1 else "") + prev
        ans = min(ans, len(comp))
    return ans