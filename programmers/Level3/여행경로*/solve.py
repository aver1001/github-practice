def solution(tickets):
    table = {}
    N = len(tickets)+1
    
    for a,b in tickets:
        if a not in table:
            table[a] =[b]
        else:
            table[a].append(b)
            
    for i in list(table.keys()):
        table[i].sort()
        
    start  = ['ICN']
    answer = []
    cnt = 1
    while start:
        ## 만약 항공권이 있으면
        if start[-1] in table and len(table[start[-1]]) != 0:
            target = table[start[-1]].pop(0)
            start.append(target)
        ## 항공권이 없다면 
        else: 
            answer.append(start.pop())
            
    answer.reverse()
    return answer
