def solution(s):
    answer = []
    for num in s:
        #print('Start')
        #print(num)
        pt = 0
        while (True):
            try:
                
                index = num[pt:].index('110')
                if pt != 0:
                    index += 4
                #print('index',index)
                ## a[:index] + a[index:index+3] + a[index+3:]
                temp = num[:index] + num[index+3:]

                for idx in range (len(temp)):
                    if num > (temp[:idx] + '110' + temp[idx:]):
                        num = (temp[:idx] + '110' + temp[idx:])
                        pt = idx+3
                        #print(num)
                        break
                else:
                    break
                
            except:
                break
        
            
        answer.append(num)

    return answer


solution(["1110","100111100","0111111010"])
