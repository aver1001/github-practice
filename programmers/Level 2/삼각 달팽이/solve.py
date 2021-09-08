def solution(n):
    temp = [[0 for _ in range(n)]for _ in range (n)]
    add = [[1,0],[-1,1],[0,-1]]
    answer = []
    x = 0
    y = 0
    turn = 0
    check = [i for i in range (1,n+1)]
    turnTime = check.pop()
    for i in range (1, int((n+1)*n/2)+1):
        temp[x][y] = i
        turnTime -= 1
        if turnTime == 0 and len(check) != 0:
            turnTime = check.pop()
            if turn != 2:
                turn +=1
            else:
                turn = 0
        x += add[turn][0]
        y += add[turn][1]
    
    for i in range(n+1):
        ax = i-1
        ay = 0
        for j in range (i):
            answer.append(temp[ax][ay])
            ax -= 1
            ay += 1
    return(answer)

solution(6)

    
