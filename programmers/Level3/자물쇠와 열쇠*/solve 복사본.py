def rotation(arr):
    n = len(arr)
    temp = [[]for _ in range (n)]
    for i in range (n-1,-1,-1):
        for j in range (n):
            temp[j].append(arr[i][j])
    return temp

def isCorrect(x,y,table,key):

    N = len(key)
    temp = [[0 for _ in range (len(table))]for _ in range (len(table))]
    for i in range (len(table)):
        for j in range (len(table)):
            temp[i][j] = table[i][j]
    for i in range (N):
        for j in range (N):
            temp[x+i][y+j] = table[x+i][y+j] + key[i][j]

    for i in temp : print(i)
    for i in range (N):
        for j in range (N):
            if temp[2+i][2+j] != 1:
                return False
    return True
    
            
                    
            
            
    


def solution(key, lock):
    # 항상 키가 더 작음 
    keyN = len(key)
    lockN = len(lock)
    N = keyN*2 + lockN -2
    table = []
    table =[[0 for _ in range (N)]for _ in range (keyN-1)]
    for i in lock:
        temp = [0 for _ in range (keyN-1)]
        temp.extend(i)
        temp.extend([0 for _ in range (keyN-1)])
        table.append(temp)
    table.extend([[0 for _ in range (N)]for _ in range (keyN-1)])
    for i in table : print(i)

    for _ in range (4):
        for x in range (len(table) - len(key)):
            for y in range (len(table) - len(key)):
                if isCorrect(x,y,table,key) :
                    return True

        table = rotation(table)    
        
                        
            
    return False

                    
                
                

    
    

a = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(a)
