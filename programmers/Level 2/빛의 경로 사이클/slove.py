import time

def solution(grid):
    visited = []
    
    Max_x = len(grid)
    Max_y = len(grid[0])

    board = [[0]*Max_y for _ in range(Max_x)]
    
    for i,direction in enumerate(grid):
        temp = []
        for j,direct in enumerate(direction):
            temp.append([0,0,0,0])
            board[i][j] = direct
        visited.append(temp)

    ## [12,3,6,9]
    for i in board: print(i)
    print()
    for i in visited: print(i)
    
    answer = []
    cnt = 0
    for i in range (Max_x):
        for j in range (Max_y):
            for k in range (4):
                x,y = i,j
                if k == 0:
                    before = 0
                elif k == 1:
                    before = 1
                elif k == 2:
                    before = 2
                elif k == 3:
                    before = 3
                
                cnt = 0
                while (visited[x][y][before] == 0):
                    ## 방문한거 체크

                    visited[x][y][before] = 1 

                    cnt += 1
                    print(x,y,before,board[x][y],cnt)
                    
                    for q in visited: print(q)
                    
                    ## 이동
                    if board[x][y] == 'S':
                        
                        if before == 0:
                            x += 1
                        elif before == 1:
                            y -= 1
                        elif before == 2:
                            x -= 1
                        elif before == 3:
                            y += 1
                            
                            
                    elif board[x][y] == 'L':
                        
                        if before == 0:
                            y += 1
                            before = 3
                        elif before == 1:
                            x += 1
                            before = 0
                        elif before == 2:
                            y -= 1
                            before = 1
                        elif before == 3:
                            x -= 1
                            before = 2
                            
                    elif board[x][y] == 'R':
                        
                        if before == 0:
                            y -= 1
                            before = 1
                        elif before == 1:
                            x -= 1
                            before = 2
                        elif before == 2:
                            y += 1
                            before = 3
                        elif before == 3:
                            x += 1
                            before = 0
                            
                    if x == -1:
                        x = Max_x-1
                    if y == -1:
                        y = Max_y-1
                    if x == Max_x:
                        x = 0
                    if y == Max_y:
                        y = 0
                    time.sleep(0.5)
                    
                if cnt != 0:
                    answer.append(cnt)
            
    print(answer)




solution(["SL","LR"]) ## [16]