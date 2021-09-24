def solution(lines):
    times = []
    for i in lines:
        days, hours, sec =i.split(' ')
        tempD,tempS= hours.split('.')
        h,m,s = map(int,tempD.split(':'))
        hours = h*3600 + m*60 + s+ float('0.'+tempS)
        times.append([hours-float(sec.replace('s','')),hours])
    Max = 0

    for i in range(len(times)):
        print(times[i],end = ' ')
        cnt = 0
        for j in range (i,len(times)):
            if times[j][0] >= times[i][1] +1-0.001:
                break
            cnt +=1
        
        if cnt > Max:
            Max = cnt
        print(cnt)
    return(Max)
                
        
        

        

a = solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
'''
def solution(lines):
    times = []
    for i in lines:
        days, hours, sec =i.split(' ')
        tempD,tempS= hours.split('.')
        h,m,s = map(int,tempD.split(':'))
        hours = h*3600 + m*60 + s+ float('0.'+tempS)
        times.append([hours-float(sec.replace('s','')),hours])
    Max = 0

    for a in times:
        cnt = 0
        for start,end in times:
            if a[1]-0.001 <= start <a[1]+1-0.001 or a[1]-0.001 <= end < a[1]+1-0.001:
                cnt += 1
        if cnt > Max:
            Max = cnt
    return(Max)
'''
