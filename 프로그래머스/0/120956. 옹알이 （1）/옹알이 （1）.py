def solution(babbling):
    A = ["aya", "ye", "woo", "ma"]
    ans = 0
    
    for i in range(len(babbling)):
        for word in A:
            if word in babbling[i]:
                babbling[i] = babbling[i].replace(word, "#")
        if all(char == "#" for char in babbling[i]):
            ans += 1
    return ans