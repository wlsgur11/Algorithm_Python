num = list(map(str, input().split()))
​
num.sort(key=lambda x: x*3, reverse=True)
ans = ''.join(num)
print(str(int(ans)))