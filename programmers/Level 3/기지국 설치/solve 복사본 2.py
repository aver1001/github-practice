

def solution(n, stations, w):
    power = w*2+1
    ## 이미 설치된 기지국 확인
    pt = 1
    answer = 0
    for index in stations:
        print(index-w,index+w)
        temp = index - w - pt
        if temp % power == 0:
            answer += temp // power
            print('Build',temp // power)
        else:
            answer += temp // power + 1
            print('Build',temp // power + 1)
            
        pt = index+w+1
    pt -= 1
    if pt <= n:
        
        temp = n - pt
        if temp % power == 0:
            answer += temp // power
        else:
            answer += temp // power + 1


    print(answer)
    return(answer)


solution(16,[3,4,9,13],2)
