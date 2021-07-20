'''


'''
import sys
import time
import copy
sys.setrecursionlimit(10**6)

def printGoal(road) :
    
    for i in road:
        print(i)

def addNone(arr):
    
    for i in arr:
        i.insert(0,0)
        i.append(0)
        
    arr.insert(0,[0]*(n+2))
    arr.insert(n+1,[0]*(n+2))

    return arr

def findMax (road):
    Max = 0

    for i in range(1,n+1):
        for j in range (1,n+1):
            if road[i][j] > Max:
                Max = road[i][j]

    return Max

def findMin (road):
    Min = 9999

    for i in range(1,n+1):
        for j in range (1,n+1):
            if road[i][j] < Min:
                Min = road[i][j]

    return Min


def findHouses(x,y,road,num) :
    #print(x,y,road[x][y],"0으로 변경")
    road[x][y] = 0

        ##상
    if road[x-1][y] >= num:
        findHouses(x-1,y,road,num)
        ##하
    if road[x+1][y] >= num:
        findHouses(x+1,y,road,num)
        ##좌
    if road[x][y-1] >= num:
        findHouses(x,y-1,road,num)
        ##우
    if road[x][y+1] >= num:
        findHouses(x,y+1,road,num)

    return road


def copyArr(arr):
    temps = [0]*(n+2)
    temps = [temps]*(n+2)

    for i in range (n+2):
        for j in range (n+2):
            #print(temp[i][j] , '=' ,arr[i][j])
            temps[i][j] = arr[i][j]
    #print(arr)
    return temps

def findSafe(arr):
    
    global cnt
    global maxs
    for i in range (findMin(arr),findMax(arr)):
        cnt = 0
        temp = copy.deepcopy(arr)
        #printGoal(temp)
        for j in range (1,n+1):
            for k in range (1,n+1):
                if temp[j][k] >= i :
                    #print(j,k,i,"보다 작은값 확인")
                    cnt +=1
                    temp = findHouses(j,k,temp,i)
            
        #print("단지수 : ",cnt)
        if cnt > maxs :
            maxs = cnt
        
                    
    
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list()
    global maxs
    maxs = 0
    for i in range (n):
        a.append(list(map(int,input().split())))

    a = addNone(a)
    #printGoal(a)

    findSafe(a)
    print(maxs)
    '''
    global cnt
    cnt = 1

    for i in range(1,n+1):
        for j in range (1,n+1):
            if a[i][j] == 1:
                cnt +=1
                a = findHouses(i,j,a)

    print(cnt-1)
    result = list()
    for i in range (2,cnt+1):
        #print(i)
        sums = 0
        for j in a:
            sums += j.count(i)
        result.append(sums)

    result.sort()
    for i in result:
        print(i)
    '''
    

    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


