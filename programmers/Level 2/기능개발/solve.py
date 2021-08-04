def solution(progresses, speeds):
    answer = list()
    
    while(progresses):
        
        for i in range (len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100: progresses[i] = 100
        print(progresses)
        cnt = 0
        if progresses[0] == 100:
            
            for i in progresses:
                if i != 100 : break
                cnt += 1
            print(cnt)
            for i in range (cnt):
                speeds.pop(progresses.index(100))
                progresses.remove(100)
        if cnt != 0 : answer.append(cnt)
            
    return answer
        
    
            
                
        
        
                

progresses = [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5, 10, 7]

print(solution(progresses,speeds))

print([1, 2, 3])
