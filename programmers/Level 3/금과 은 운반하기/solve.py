from collections import deque

## 문제를 잘못풀엇음..
## 문제를 잘 해석하고 풀 것 
def solution(a, b, g, s, w, t):
    ## a 필요한 금
    ## b 필요한 은
    ## g 갖고있는 금
    ## s 갖고있는 은
    ## t 편도 이동 시간
    ## w 운반할 수 있는 무개
    
    ## 새로운 도시를 건설하기 위해 금과 은을 전달 할 수 잇는 가장빠른시간을 return 하세요.
    
    ## 시간대비 옮길 수 있는 양 리스트를 만듦
    ## 금과 은 따로 구해야함.
    ## 운반가능 무게보다 적게있을 경우 생각해야함.
    wfort = []
    for idx in range (len(g)):
        g[idx] = [idx,g[idx],s[idx],g[idx]/t[idx],s[idx]/t[idx],t[idx],w[idx],0]
    
    ## 인덱스, 금, 은,금 처리량 ,은 처리량,시간 ,운반할 수 있는 무게, 체크
    print("인덱스, 금, 은, 처리량,처리량,용적,체크")
    g.sort(key=lambda x:-x[3])
    for i in g :print(i)
    time = 0
    check = [0] * len(g)
    pt = 0
    while(True) :
        idx,gold,silver,g_d,s_d,t,weight,check = g[pt]
        print(a,b,time)
        print(idx,gold,silver,g_d,s_d,t,weight,check)
        ##꽉 채워서 출발
        if gold+silver >= weight:
            if gold > weight and a >= 0:
                gold -= weght
                a -= weight
            else:
                weight -= gold
                a -= gold
                if silver > weight and b >= 0:
                    silver -= weight
                    b -= weight
                else:
                    b -= silver
                    
        ##자리 남음  
        else:
            if a >= 0:
                weight -= gold
                a -= gold
            if b >= 0:
                weight -= silver
                b -= silver
        if check == 0:
            #첫 주행이 끝나면 시간 2배로 변경
            g[pt][5] *= 2
            g[pt][7] = 1

        pt += 1
        time += t
        if a < 0:
            a = 0
        if b < 0:
            b = 0
        if pt >= len(g):
            pt = 0
        if a <= 0 and b <= 0:
            return time
            
    '''
    while(a >= 0 or b >= 0):
        ## 재고가 운반할수 있는 물건보다 작을경우
        ## 시간대비 옮길 수 있는 양을 바꿔줘야함
        for idx,wt in wfort:
            ## 금
            ## 만약 재고가 남아있으면
            print(g[idx],"-",w[idx],"=",g[idx]-w[idx])
            if g[idx] - w[idx] >= 0:
                g[idx] -= w[idx]
                a -= w[idx]
                time +=  2*t[idx]
                break
        for idx,wt in wfort:
            ## 은
            ## 만약 재고가 남아있으면
            if s[idx] - w[idx] >= 0:
                s[idx] -= w[idx]
                b -= w[idx]
                time += 2*t[idx]
                break
        print(a,b,time)
    '''


solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
