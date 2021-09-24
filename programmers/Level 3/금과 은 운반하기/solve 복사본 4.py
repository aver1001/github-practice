def solution(a, b, g, s, w, t):
    ## a 필요한 금
    ## b 필요한 은
    ## g 갖고있는 금
    ## s 갖고있는 은
    ## t 편도 이동 시간
    ## w 운반할 수 있는 무개
    
    ## 새로운 도시를 건설하기 위해 금과 은을 전달 할 수 잇는 가장빠른시간을 return 하세요.

    ## 가능한 가장 긴 시간을 구해준다
    Maximum = 0
    for gold,silver,weight,time in zip(g,s,w,t):
        temp = (((gold+silver) // weight)+1)*(time*2)
        if temp > Maximum:
            Maximum = temp
    
    lt ,rt =0,Maximum

    while(lt < rt):
        pt = (lt + rt) // 2
        ## 금우선 운반
        ## 운반한 금
        ## 운반한 은
        Gdegold = 0
        Gdesilver = 0
        Sdegold = 0
        Sdesilver = 0
        for gold,silver,weight,time in zip(g,s,w,t):
            deliver = weight*((pt-time)//(time*2)+1)

            #금먼져
            temp = min(gold,deliver)
            Gdegold += temp
            Gdesilver += min(silver,deliver-temp)

            #은먼져
            temp = min(silver,deliver)
            Sdesilver += temp
            Sdegold += min(gold,deliver-temp)
            #print('Time = ',pt,'\nGoldFirst : ',Gdegold,Gdesilver,'\nSilverFirst : ',Sdegold,Sdesilver)
            
        if a <= Gdegold and b <= Sdesilver and a+b <= Sdegold+Sdesilver:
            rt = pt
        else:
            lt = pt+1
    
    return lt
    

solution(10,10,[100],[100],[7],[10])
print("\n########\n")
solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
