def DFS(hap,floor):
    global Money,answer

    if hap >= N or floor >= len(Money):
        if hap == N:
            answer += 1
        return
    몫, 나머지 = divmod(N,Money[floor])

    for i in range (몫,-1,-1):
        print(i)
        if hap+(Money[floor]*i) <= N:
            DFS(hap +(Money[floor]*i),floor+1)
        else:
            break
    
    
    



def solution(n, money):
    global Money,N,answer
    money.sort()
    answer = 0
    N = n
    Money = list(reversed(money))

    DFS(0,0)
    return(answer)



solution(5,[1,2,5])
