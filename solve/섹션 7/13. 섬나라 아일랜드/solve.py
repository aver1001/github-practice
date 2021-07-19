'''


'''
import sys
import time


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
    global cnt
    
    road[x][y] = 2
    

        ##상
    if road[x-1][y] == 1:
        findHouses(x-1,y,road)
        ##우상
    if road[x-1][y+1] == 1:
        findHouses(x-1,y+1,road)
        ##우
    if road[x][y+1] == 1:
        findHouses(x,y+1,road)
        ##우하
    if road[x+1][y+1] == 1:
        findHouses(x+1,y+1,road)
        ##하
    if road[x+1][y] == 1:
        findHouses(x+1,y,road)
        ##좌하
    if road[x+1][y-1] == 1:
        findHouses(x+1,y-1,road)
        ##좌
    if road[x][y-1] == 1:
        findHouses(x,y-1,road)
        ##좌상
    if road[x-1][y-1] == 1:
        findHouses(x-1,y-1,road)

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
        a.append(list(map(int,input().split())))

    a = addNone(a)
    #printGoal(a)

    
    global cnt
    cnt = 0

    for i in range(1,n+1):
        for j in range (1,n+1):
            if a[i][j] == 1:
                cnt +=1
                a = findHouses(i,j,a)

    print(cnt)

    

    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


