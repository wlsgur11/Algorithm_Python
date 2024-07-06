def solution(s, n):
    result = ""
    for alp in s:
        if alp == " ":
            result += " "
        elif alp.islower():
            result += chr((ord(alp)-ord('a') + n) % 26 + ord('a'))
        elif alp.isupper():
            result += chr((ord(alp)-ord('A') + n) % 26 + ord('A'))
    return result