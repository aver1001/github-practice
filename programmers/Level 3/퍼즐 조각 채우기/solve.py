

def findBlock(arr,blank,fill):
    n = len(arr)
    Block = []
    
    for x in range(n):
        for y in range(n):
            print(x,y)
            if arr[x][y] == blank:
                temp_X = []
                temp_Y = []
                queue = [[x,y]]
                while(queue):
                    tx,ty = queue.pop(0)
                    arr[tx][ty] = fill
                    for i in arr: print(i)
                    print()
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
                        
                Block.append(list(map(list,(zip(temp_X,temp_Y)))))
                
    for i in Block: print(i)
    return Block
                        
                
def rotation(arr):
    Max = 0
    for x,y in arr:
        if x > Max:
            Max = x
        if y > Max:
            Max = y
    temp = [[0 for _ in range(Max)]for _ in range (Max)]
    
        
        
    
        

def solution(game_board, table):
    for a,b in zip(game_board,table):print(a," ",b)
    print()
    boardBlock = findBlock(game_board,0,1)
    print()
    tableBlock = findBlock(table,1,0)

    


solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
         ,[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
