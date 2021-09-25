def solution(routes):
    
    routes.sort(key = lambda x:x[1])
    checkpoint = routes[0][1]
    cnt = 1
    for start,end in routes:
        if start > checkpoint and checkpoint < end :
            checkpoint = end
            cnt += 1
    return(cnt)
            
    





solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
