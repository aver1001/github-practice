def solution(s):
    ## 110 다 없애버리고 붙여버리기
    answer = []
    
    for num in s:
        ## a[:index] + a[index:index+3] + a[index+3:]
        
        ## 110 다 없앰
        cnt = 0
        stack = ''
        for i in num:
            if i == '0' and stack[-2:] == '11':
                stack = stack[:-2]
                cnt += 1
            else:
                stack += i

        if stack == '1':
            answer.append('110'*cnt + '1')
        else:
            ## 11 찾아서 그 앞에 110 * cnt 넣어줌
            find = stack.find('11')
            if find != -1:
                index = stack.index('11')
            else:
                index = stack.rindex('0')+1
            answer.append(stack[:index]+'110'*cnt+stack[index:])

    return answer


solution(["1110","100111100","0111111010"])
