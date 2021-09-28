def solution(a):
    table = {}
    N = len(a)
    if 1 >= N:
        return 0
    for i in a:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    temp = list(table.items())
    temp.sort(key = lambda x:-x[1])
    
    print(temp)
    answer = 0
    for check,count in temp:
        pt = 0
        temp = 0
        if count*2 < answer :
            continue
        else:
            while(pt+1 < N):
                print(a[pt],a[pt+1],end = '')
                if (a[pt] == check and a[pt+1] != check) or (a[pt] != check and a[pt+1] == check):
                    temp += 2
                    pt += 2
                    print('##')
                else:
                    pt += 1
                    print()
        if temp > answer:
            answer = temp

    print(answer)
    return(answer)


        
    


solution([0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4])
