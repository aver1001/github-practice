def calTime(timetable):
    for index,time in enumerate(timetable):
        hour,minute = map(int,time.split(':'))
        timetable[index] = hour*60 + minute
    
    return timetable

def changeTime(minute):
    return str(minute // 60).zfill(2) + ':' + str(minute % 60).zfill(2)

def solution(n, t, m, timetable):

    
    
    timetable = calTime(timetable)
    timetable.sort()
    timetable.append(-1)
    
    pt = 0
    
    for time in range (540,540+(t*(n-1)+1),t):
        for _ in range (m):
            if timetable[pt] == -1:
                return changeTime(540+(t*(n-1)))
            elif timetable[pt] <= time:
                pt += 1
                
    if pt == 0:
        return changeTime(time)
    else:
        return changeTime(timetable[pt-1]-1)            
## 18번 테스트 케이스만 안되는데 도대체 뭔지 모르겟음..             
    

    
                
                
            


solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])
