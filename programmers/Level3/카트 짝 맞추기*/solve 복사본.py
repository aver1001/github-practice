def solution(board, r, c):

    '''
    실패
    다른카드로 가는길에 카드가 존재할 경우를 생각하지 않았음.


    '''








    
    for i in board: print(i)
    #x,y = r,c

    ## 입력크기 board 는 4*4 이므로 복잡도는 신경 쓰지않고 풀어보자

    table = []
    ## 일단 카드 있는 곳들을 저장하자
    for x in range (4):
        for y in range (4):
            if board[x][y] != 0:
                table.append([board[x][y],x,y])

    x,y = r,c
    card = 0
    choose = 0
    cnt = 0
    while table:
    ## 카드 == 0
        print(table,cnt)
        if card == 0:
        ## 만약 자신위치에 카드가 있다면 카드 선택 : 카드 += 1 , continue
            if board[x][y] != 0:
                choose = board[x][y]
                board[x][y] = 0
                card = 1
                cnt += 1
                table.remove([choose,x,y])
                continue
        ## 가장 가까운 카드로 이동 (어디있던 두번안에 이동 가능)
        ## 상하좌우 한번에 이동 가능할 경우 이동: 카드 += 1, continue
            ##카드들을 확인하며
            for idx,ax,ay in table:
                ## x,y중 하나가 같고
                if ay == y:
                    ## 중간에 막는게 없다면 
                    if ax > x and all(board[i][y] == 0 for i in range(x+1,ax)):
                        choose = idx
                        board[ax][ay] = 0
                        card = 1
                        table.remove([idx,ax,ay])
                        cnt += 2
                        x,y = ax,ay
                        break
                    elif ax < x and all(board[i][y] == 0 for i in range(ax+1,x)):
                        choose = idx
                        board[ax][ay] = 0
                        card = 1
                        table.remove([idx,ax,ay])
                        cnt += 2
                        x,y = ax,ay
                        break
                elif ax ==x:

                    if ay > y and all(board[x][i] == 0 for i in range(y+1,ay)):
                        choose = idx
                        board[ax][ay] = 0
                        card = 1
                        table.remove([idx,ax,ay])
                        cnt += 2
                        x,y = ax,ay
                        break
                    elif ay < y and all(board[x][i] == 0 for i in range (ay+1,y)):
                        choose = idx
                        board[ax][ay] = 0
                        card = 1
                        table.remove([idx,ax,ay])
                        cnt += 2
                        x,y = ax,ay
                        break
        ##  한번에 이동이 안될경우 두번에 이동(아무거나 선택??)
            else:
                idx,ax,ay = table.pop(0)
                choose = idx
                board[ax][ay] = 0
                card = 1
                cnt += 3
                x,y = ax,ay
                continue
        ##  이동: 카드 += 1, continue
    
    ## 카드 == 1
        if card == 1:
        ## 자신과 같은 카드로 이동
            for idx,ax,ay in table:
                if choose == idx:
                ## 한번에 이동: 카드 = 0, continue
                    if ay == y:
                        ## 중간에 막는게 없다면 
                        if ax > x and all(board[i][y] == 0 for i in range(x+1,ax)):
                            board[ax][ay] = 0
                            card = 0
                            table.remove([idx,ax,ay])
                            cnt += 2
                            x,y = ax,ay
                            break
                        elif ax < x and all(board[i][y] == 0 for i in range(ax+1,x)):
                            board[ax][ay] = 0
                            card = 0
                            table.remove([idx,ax,ay])
                            cnt += 2
                            x,y = ax,ay
                            break
                    elif ax ==x:

                        if ay > y and all(board[x][i] == 0 for i in range(y+1,ay)):
                            board[ax][ay] = 0
                            card = 0
                            table.remove([idx,ax,ay])
                            cnt += 2
                            x,y = ax,ay
                            break
                        elif ay < y and all(board[x][i] == 0 for i in range (ay+1,y)):
                            board[ax][ay] = 0
                            card = 0
                            table.remove([idx,ax,ay])
                            cnt += 2
                            x,y = ax,ay
                            break
            
                ## 두번에 이동: 카드 = 0, continue
                    board[ax][ay] = 0
                    card = 0
                    table.remove([idx,ax,ay])
                    cnt += 3
                    x,y = ax,ay
        
    print(cnt)
        
solution([[0,0,0,3],[2,1,0,2],[0,0,0,0],[3,0,1,0]],1,0)
