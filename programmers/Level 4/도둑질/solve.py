def solution(money):
    N = len(money)
    table1 = [0]*N
    table2 = [0]*N
    ## 첫집을 털었을떄
    table1[0] = money[0]
    table1[1] = money[0]
    for i in range (2,N-1):
        table1[i] = max(table1[i-1], table1[i-2]+money[i])
    ## 첫집을 못털었을때
    table2[1] = money[1]
    for i in range(2,N):
        table2[i] = max(table2[i-1],table2[i-2]+money[i])
    
    return max(table1[-2],table2[-1])
