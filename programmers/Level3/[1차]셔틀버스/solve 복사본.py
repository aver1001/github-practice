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

    time = 540
    pt = 0
    for _ in range (n):
        for _ in range (m):
            if pt == len(timetable):
                    print("??")
                    return changeTime(540 +(n*(t-1)))
            if timetable[pt] <= time:
                pt += 1
            else:
                break
                ## 탈사람 다탓음
                
            print(pt)
        time += t
    
    if pt-1 <= len(timetable) :
        return changeTime(timetable[pt-1]-1)
    else:
        return changeTime(time-t)
    
print(solution(1,1,5, ["00:01", "00:01", "00:01","00:01", "00:01", "00:02", "00:03", "00:04"]))
