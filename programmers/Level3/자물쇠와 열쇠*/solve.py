def rotation(arr):
    n = len(arr)
    temp = [[]for _ in range (n)]
    for i in range (n-1,-1,-1):
        for j in range (n):
            temp[j].append(arr[i][j])
    return temp
            
def isCorrect(x,y,temp,lock):
    for i in temp: print (i)
    print()
    for i in lock: print (i)
    for i in range (len(lock)):
        for j in range (len(lock)):
            if [i,j] not in temp and lock[i][j] == 0:
                return False
    return True
            
    


def solution(key, lock):
    temp = []
    keyn = len(key)
    lockn = len(lock)
    minX = 999
    minY = 999
    for i in range (lockn):
        for j in range (lockn):
            if lock[i][j] == 0:
                temp.append([i,j])
                if minX > i:
                    minX = i
                if minY > j:
                    minY = j

                
    for i in range(len(temp)) :
        temp[i][0] -= minX
        temp[i][1] -= minY
    
    lenX = len(temp)
    lenY = len(temp[0])
    print("LenY",lenY)
    for _ in range (4):
        for a,b in zip(key,lock) : print(a,"  ",b)
        for i in range(keyn-lenX+1):
            for j in range (keyn-lenY+1):
                print(isCorrect(i,j,temp,lock))
                if isCorrect(i,j,temp,lock):
                    return True
        lock = rotation(lock)
        print("##########rotatoin##########")
        
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
