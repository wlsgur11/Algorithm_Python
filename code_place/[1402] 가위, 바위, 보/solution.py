a, b = map(int, input().split())
if a < 4 and a > 0 and b < 4 and b > 0:
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("A승B패")
    elif (a == 2 and b == 3) or (a == 3 and b == 1) or (a == 1 and b == 2):
        print("B승A패")
    else:
        print("무승부")
else:
    print("잘못된입력")