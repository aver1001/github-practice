def solution(genres, plays):
    
    table = {}
    total = {}
    for index , (genre,plays) in enumerate(zip(genres,plays)):
        
        if genre not in table:
            table[genre] = [[index,plays],[-1,0]]
            total[genre] = plays
        else:
            table[genre].append([index,plays])
            table[genre].sort()
            table[genre].sort(reverse = True , key = lambda x:x[1])
            table[genre] = table[genre][:2]
            total[genre] = total[genre] +plays
            
    total = sorted(total.items(),key = lambda x: x[1],reverse = True)
            
    answer = []
    
    for name,num in total:
        for a,b in table[name]:
            if a != -1:
                answer.append(a)
    

    return answer
a = solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000])

[[[1, 500], [3, 150]], [4, 800]]
