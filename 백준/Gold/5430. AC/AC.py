from collections import deque
import sys

N = int(input())

for i in range(N):
    fun = sys.stdin.readline()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1

    ans = 1
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in fun:
        if j == "R":
            rev += 1
        elif j == "D":
            if len(queue) < 1:
                ans = 0
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if ans == 1:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")