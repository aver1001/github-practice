'''


'''
import sys
import time
import copy

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



def findHouses(x,y,road) :
    print(x,y,road[x][y],"0으로 변경")
    road[x][y] = 0

        ##상
    if road[x-1][y] != 0:
        findHouses(x-1,y,road)
        ##하
    if road[x+1][y] != 0:
        findHouses(x+1,y,road)
        ##좌
    if road[x][y-1] != 0:
        findHouses(x,y-1,road)
        ##우
    if road[x][y+1] != 0:
        findHouses(x,y+1,road)

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
    for i in range (1,101):
        print(i,"보다 작은 값 0으로 변경")
        temp = copy.deepcopy(arr)
        cnt = 0
        for j in range (n+1):
            for k in range(n+1):
                if temp[j][k] <= i:
                    temp[j][k] = 0

        printGoal(temp)

        ## i보다 작은거 0 으로 변경 완료
        for j in range (1,n+1):
            for k in range (1,n+1):
                if temp[j][k] != 0 :
                    print("0이 아닌값 확인")
                    cnt +=1
                    temp = findHouses(j,k,temp)
            
        print("단지수 : ",cnt)
        if cnt > maxs :
            maxs = cnt
        
                    
    
        
start = time.time()
for sn in range (1,2):
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

    


