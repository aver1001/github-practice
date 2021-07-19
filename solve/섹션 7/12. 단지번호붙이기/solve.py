'''


'''
import sys
import time


def printGoal(road) :
    
    for i in road:
        print(i)

        
def strToint(arr):
    
    for i in range (n):
        for j in range (n):
            arr[i][j]=int(arr[i][j])

    return arr

def addNone(arr):
    
    for i in arr:
        i.insert(0,0)
        i.append(0)
        
    arr.insert(0,[0]*(n+2))
    arr.insert(n+1,[0]*(n+2))

    return arr

def findHouses(x,y,road) :
    global cnt
    
    road[x][y] = cnt

        ##상
    if road[x-1][y] == 1:
        findHouses(x-1,y,road)
        ##하
    if road[x+1][y] == 1:
        findHouses(x+1,y,road)
        ##좌
    if road[x][y-1] == 1:
        findHouses(x,y-1,road)
        ##우
    if road[x][y+1] == 1:
        findHouses(x,y+1,road)

    return road
        
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
    for i in range (n):
        a.append(list(input()))

    a = strToint(a)
    a = addNone(a)
    
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
                

    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


