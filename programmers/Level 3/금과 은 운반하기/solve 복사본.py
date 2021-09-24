def solution(a, b, g, s, w, t):
    ## a 필요한 금
    ## b 필요한 은
    ## g 갖고있는 금
    ## s 갖고있는 은
    ## w 운반할 수 있는 무개
    ## t 편도 이동 시간
    
    ## 새로운 도시를 건설하기 위해 금과 은을 전달 할 수 잇는 가장빠른시간을 return 하세요.
    
    table = list(map(list,zip(g,s,w,t,t)))
    table.sort(key = lambda x:x[3])

    ts, tg = 0 , 0
    for aa,bb,cc,dd,ee in table:
        ts += cc / ee
        tg += dd / ee

    while(True):

        gold, silver, weight, time,q = table[0]
        print(a,b)
        ## 많이 필요한거 우선적으로 옮겨준다
        if a/ts >= b/ts :
            ## 금을 최대한 가져간다
            subtract = min(a,gold,weight)
            a -= subtract
            gold -= subtract
            weight -= subtract
            ## 남은걸 은으로 채운다 
            subtract = min(b,silver,weight)
            b -= subtract
            silver -= subtract
            weight -= subtract
        else:
            ## 은을 최대한 가져간다
            subtract = min(b,silver,weight)
            b -= subtract
            silver -= subtract
            weight -= subtract
            ## 남은걸 금으로 채운다
            subtract = min(a,gold,weight)
            a -= subtract
            gold -= subtract
            weight -= subtract
            
        ## 한번 갔으면 시간 2배로
        table[0][3] += 2*table[0][4]
        if a == 0 and b == 0:
            return time
        table.sort(key = lambda x:x[3])
        

    return(time)
    
    
    
    
    


solution(10,10,[100],[100],[7],[10])
