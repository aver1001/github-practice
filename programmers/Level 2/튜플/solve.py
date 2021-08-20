def solution(s):
    answer = []
    temp = []
    result = []
    res = ''
    for i in s[1:len(s)-1]:
        #print(i, res,temp, result)
        if i == '{':
            temp = set()
        elif i == '}':
            result.append(temp)
        elif i == ',':
            temp.add(int(res))
            res = ''
        else :
            res += i
    result[-1].add(int(res))
    temp = [0]*len(result)
    for i in result:
        temp[len(i)-1] = i

    answer.append(list(temp[0])[0])
    for i in range(0,len(temp)-1):
        answer.append(list(temp[i+1] - temp[i])[0])
    
        
    
    return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
result = [2, 1, 3, 4]

print(solution(s))


## 배운점
## sort 할때 key 값에 len 이 들어갈 수 있다.
