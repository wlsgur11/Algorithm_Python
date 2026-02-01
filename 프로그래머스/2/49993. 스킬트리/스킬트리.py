def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        fillter = "".join([s for s in tree if s in skill])
        if skill.startswith(fillter):
            ans += 1
    return ans