import sys

N = int(sys.stdin.readline())
dic = {}
arr = []
for i in range(N):
    A = int(sys.stdin.readline())    
    arr.append(A)
arr.sort()
for i in arr:
    if i in dic: dic[i] += 1
    else: dic[i] = 1
mx = max(dic.values())
mx_dic = []
print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
for i in dic: 
    if mx == dic[i]: mx_dic.append(i)
if len(mx_dic) > 1: print(mx_dic[1])
else: print(mx_dic[0])
print(arr[-1] - arr[0])