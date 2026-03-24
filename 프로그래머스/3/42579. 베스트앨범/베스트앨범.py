def solution(genres, plays):
    stream = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in stream.keys():
            stream[g] = [(i, p)]
        else:
            stream[g].append((i, p))
            
    sorted_genres = sorted(stream.items(), 
                           key=lambda x: sum(song[1] for song in x[1]), 
                           reverse=True)

    answer = []
    
    for genre, songs in sorted_genres:
        songs.sort(key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in songs[:2]])
        
    return answer