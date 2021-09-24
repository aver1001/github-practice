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
        print(lt,rt,pt)
        ## 금우선 운반
        ## 운반한 금
        ## 운반한 은
        Gdegold = 0
        Gdesilver = 0
        Sdegold = 0
        Sdesilver = 0
        for gold,silver,weight,time in zip(g,s,w,t):
            # 지정된 시간동안 배달한 양
            if pt > time:
                deliver = weight * (((pt-time)//(time*2))+1)
            else:
                deliver = 0
                continue
                
            if deliver >= gold + silver:
                deliver = gold + silver
            

            ## 요부분 부터 다시 코딩
            
            
            ## 금 우선일경우
            if gold > deliver:
                Gdegold += deliver
                Gdesilver += 0
            else:
                Gdegold += gold
                Gdesilver += deliver - gold
            ## 은 우선일경우
            if silver > deliver :
                Sdesilver += deliver
                Sdegold += 0
            else:
                Sdesilver += silver
                Sdesilver += deliver - silver
            print(Gdegold,Gdesilver,Sdegold,Sdesilver)
        print(a,'<=',Gdegold,'    ',b,'<=',Sdesilver, a+b,'<',Gdegold+Gdesilver)
        if a <= Gdegold and b <= Sdesilver and a+b <= Sdegold+Sdesilver:
            rt = pt
        else:
            lt = pt+1
        print()
    

solution(10,10,[100],[100],[7],[10])
print("\n########\n")
solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
