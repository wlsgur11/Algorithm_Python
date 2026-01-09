def solution(keymap, targets):
    keys_dict = {}
    for key in keymap:
        for k in range(len(key)):
            if key[k] not in keys_dict.keys():
                keys_dict[key[k]] = k + 1
            else:
                if (k+1) < keys_dict[key[k]]:
                    keys_dict[key[k]] = k + 1
    ans = [0 for _ in range(len(targets))]
    for i in range(len(targets)):
        for c in targets[i]:
            if c in keys_dict.keys():
                ans[i] += keys_dict[c]
            else:
                ans[i] = -1
                break
    return ans