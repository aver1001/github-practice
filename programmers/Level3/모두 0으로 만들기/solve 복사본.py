def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    table = {}
    
    for x,y in edges:
        if x not in table:
            table[x] = [y]
        else:
            table[x].append(y)
        if y not in table:
            table[y] = [x]
        else:
            table[y].append(x)
    answer = 0
    for i in range (len(a)):
        for idx, weight in enumerate(a):
            # 가중치가 0이 아닐 경우
            if weight != 0 and len(table[idx]) == i:
                if idx in table:
                    for y in table[idx]:
                        if a[y] != 0:
                            temp = a[idx]
                            a[idx] = 0
                            a[y] += temp
                            answer += abs(temp)
                            '''
                            if a[y] < 0:
                                a[idx] = 0
                                a[y] += weight
                                answer += abs(weight)
                            elif a[y] > 0:
                                a[idx] = 0
                                a[y] -= weight
                                answer += abs(weight)
                            '''
            # 가중치가 0일경우
            else: 
                continue
    return(answer)
