def solution(word):
    words = []
    vowel = ['A', 'E', 'I', 'O', 'U']

    def dfs(current_word):
        if current_word != '':
            words.append(current_word)
        
        if len(current_word) == 5:
            return
        
        for v in vowel:
            dfs(current_word + v)
    
    dfs('')
    
    return words.index(word) + 1