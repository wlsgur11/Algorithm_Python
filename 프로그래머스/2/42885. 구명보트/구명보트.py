def solution(people, limit):
    people.sort()
    cnt, left, right = 0, 0, len(people)-1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1
    return cnt


