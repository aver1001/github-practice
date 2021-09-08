def solution(people, limit):
    people.sort()
    cnt = 0
    lt,rt = 0, len(people)-1
    while(lt < rt):
        print(people[lt:rt+1],people[lt],people[rt])
        if people[lt]+people[rt] <= limit:
            lt += 1
        rt -= 1
        cnt += 1
        
    if lt == rt:
        cnt += 1
    return cnt
        

            
            



print(solution([70,80,50,50],100))
