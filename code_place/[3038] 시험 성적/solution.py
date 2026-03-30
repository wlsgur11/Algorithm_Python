A = int(input())
B = int(input())
​
if A >= 80 and B >= 80:
    print("합격")
elif A >= 80 or B >= 80:
    print("재수강")
else:
    print("불합격")