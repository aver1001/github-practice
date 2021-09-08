def calTime(timetable):
    for index,time in enumerate(timetable):
        hour,minute = map(int,time.split(':'))
        timetable[index] = hour*60 + minute
    
    return timetable

def solution(n, t, m, timetable):
    
    timetable = calTime(timetable)
    timetable.sort()
    person = len(timetable)
    time = 540
    pt = 0
    for _ in range (n):
        for _ in range (m):
            ## 출발시간 전에 왓을경우
            if timetable[pt] <= time:
                #태움
                pt += 1
                # 자리가 남을경우 
                if pt+1 >= person:
                    #마지막사람보다 1분 빨리 도착해야함
                    return str(time//60).zfill(2) + ':' +str(time%60).zfill(2)
                
        time += t
    ##자리가 남을경우
    return str((timetable[pt]-1)//60).zfill(2) + ':' +str((timetable[pt]-1)%60).zfill(2)

print(solution(2,10,2,["09:10", "09:09", "08:00"]))
