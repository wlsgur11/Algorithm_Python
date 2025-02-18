import sys

N, M, inven = map(int, sys.stdin.readline().split())
blocks = []

for _ in range(N):
    blocks.extend(map(int, sys.stdin.readline().split()))

min_h = min(blocks)
max_h = max(blocks)

answer_time = float('inf')
answer_height = 0

for target in range(min_h, max_h + 1):
    remove_blocks = 0
    add_blocks = 0

    for height in blocks:
        if height > target:
            remove_blocks += (height - target)
        elif height < target:
            add_blocks += (target - height)

    if remove_blocks + inven >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time <= answer_time:
            answer_time = time
            answer_height = target

print(answer_time, answer_height)