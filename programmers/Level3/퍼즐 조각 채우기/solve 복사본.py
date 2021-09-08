

def findBlock(arr,blank,fill):
    n = len(arr)
    Block = []
    
    for x in range(n):
        for y in range(n):
            if arr[x][y] == blank:
                temp_X = []
                temp_Y = []
                queue = [[x,y]]
                while(queue):
                    tx,ty = queue.pop(0)
                    arr[tx][ty] = fill
                    temp_X.append(tx)
                    temp_Y.append(ty)
                    #up
                    if tx > 0 and arr[tx-1][ty] == blank:
                        queue.append([tx-1,ty])
                    #right
                    if ty < n-1 and arr[tx][ty+1] == blank:
                        queue.append([tx,ty+1])
                    #down
                    if tx < n-1 and arr[tx+1][ty] == blank:
                        queue.append([tx+1,ty])
                    #left 
                    if ty > 0 and arr[tx][ty-1] == blank:
                        queue.append([tx,ty-1])
                        
                subtraction = min(temp_X)
                if subtraction != 0:
                    for i in range (len(temp_X)):
                        temp_X[i] -= subtraction
                subtraction = min(temp_Y)
                if subtraction != 0:
                    for i in range (len(temp_Y)):
                        temp_Y[i] -= subtraction

                Max = max(max(temp_X),max(temp_Y))
                res = [[0 for _ in range(Max+1)]for _ in range (Max+1)]
                for a,b in zip(temp_X,temp_Y):
                    res[a][b] = 1
                    
                Block.append(res)
    return Block
                        
                
def rotation(arr):
    n = len(arr)
    temp = [[]for _ in range (n)]
    check = 0
    for i in range (n-1,-1,-1):
        if arr[i].count(1) == 0:
            check += 1
            continue
        for j in range (n):
            temp[j].append(arr[i][j])

    for i in range(check):
        for j in range(n):
            temp[j].append(0)
            
    return temp
            
    
    
        
        
    
        

def solution(game_board, table):
    boardBlock = findBlock(game_board,0,1)
    tableBlock = findBlock(table,1,0)
    count = 0
    for i in tableBlock:
        for _ in range (4):
            if i in boardBlock:
                for line in i:
                    count += line.count(1)
                boardBlock.remove(i)
                break
            i = rotation(i)
    return(count)
                

    


solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
         [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]])
