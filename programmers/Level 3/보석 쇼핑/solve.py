def solution(gems):
    N = len(set(gems))
    variety = {}
    pt = 0
    Min = 999999

        
    for index,gem in enumerate(gems,start = 1):
        if gem not in variety:
            variety[gem] = 1
        else:
            variety[gem] += 1
        
        
        while(True):
            if variety[gems[pt]] >= 2:
                pt += 1
                variety[gems[pt-1]] -= 1
            else :
                break
        
        if len(variety) == N:
            if index-pt == N:
                return [pt+1,index]
            if Min > index-pt:
                answer= [pt+1,index]
                Min = index-pt
            
        
    
    return(answer)

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
