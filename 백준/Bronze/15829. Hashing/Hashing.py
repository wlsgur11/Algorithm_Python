L = int(input())
M = 1234567891
r = 31
word = input()

ans = 0

for i in range(len(word)):
    num = ord(word[i]) - 96
    ans += num * (r ** i)
print(ans % M)