def solution(a, b, g, s, w, t):
    ## a 필요한 금
    ## b 필요한 은
    ## g 갖고있는 금
    ## s 갖고있는 은
    ## w 운반할 수 있는 무개
    ## t 편도 이동 시간
    
    ## 새로운 도시를 건설하기 위해 금과 은을 전달 할 수 잇는 가장빠른시간을 return 하세요.
    
    table = list(map(list,zip(g,s,w,t)))
    table.sort(key = lambda x:x[3])
    mineral=[[0,0]for _ in range (1000)]
    ## new idea
    ## 배열을 idx를 시간으로 잡고 넣어보자.
    ## 시간별로 가능한 은의최대치, 금의 최대치를 넣어서 구해볼까
    gold,silver = 0,1
    for idx,(g,s,w,t) in enumerate(table):
        print(idx)
        times = -1
        car_time = t
        g_sum = 0
        s_sum = 0
        while(g != 0 or s != 0):
            print(times,g,s,w)
            times += 1
            
            if car_time == times:
                weight = w
                subtarct = min(g,weight)
                g -= subtarct
                weight -= subtarct
                g_sum += subtarct
                
                subtarct = min(s,weight)
                s -= subtarct
                s_sum += subtarct
                
                print("sum :",g_sum,s_sum)
                car_time += 2*t
            
            mineral[times][gold] += g_sum
            mineral[times][silver] += s_sum

            
    return mineral
            
            
    
    
    
    
    


time = solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
