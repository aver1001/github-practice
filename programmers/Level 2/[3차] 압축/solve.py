def solution(msg):
    dic = dict()
    cnt = 1
    lt,rt = 0,1
    answer = []
    for i in range (65,91):
        dic[chr(i)] = cnt
        cnt += 1
    while(True):
        while(True):
            print(msg[lt:rt])
            if dic.get(msg[lt:rt]) == None:
                print(msg[lt:rt], cnt)
                dic[msg[lt:rt]] = cnt
                answer.append(dic[msg[lt:rt-1]])
                cnt+=1
                break
            else:
                rt += 1
                if rt > len(msg):
                    answer.append(dic[msg[lt:rt-1]])
                    break
        if rt > len(msg):
            break
        lt = rt-1
        rt = lt+1
        
    print(answer)
        

solution('KAKAO')
