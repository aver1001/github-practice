def build(table,index,w):
    
    if index - w < 0:
        start = 1
    else:
        start = index - w
    if index + w > len(table)-1 :
        end = len(table)
    else:
        end = index + w+1

    for idx in range (start,end):
        table[idx] = 1
    return table

def solution(n, stations, w):
    table = [0]*(n+1)   ##전파길이 확인할 table 배열 선언 
    table[0] = 1        ##편의를 위해 n+1로 선언 후 첫번쨰 인덱스 1로 설정
    
    ## 이미 설치된 기지국 확인
    for index in stations:
        table = build(table,index,w)

        
    check = 0
    answer = 0
    for i in range (n+1):
        
        if table[i] == 0:
            if check == w:
                build(table,i,w)
                answer += 1
                check = 0
            else:
                check += 1
        elif table[i] == 1 and check != 0:
            build(table,i,w)
            answer += 1
            check = 0
    if check !=0:
        answer += 1
    return (answer)
    
        


    

        
        


solution(17,[9],2)
