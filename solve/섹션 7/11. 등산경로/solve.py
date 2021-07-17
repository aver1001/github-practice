'''


'''
import sys
import time
def printGoal(road) :
    for i in road:
        print(i)

def findMax (road):
    Max = 0

    for i in range(1,n+1):
        for j in range (1,n+1):
            if road[i][j] > Max:
                Max = road[i][j]
                Max_x = i
                Max_y = j

    #print(road[Max_x][Max_y],Max_x,Max_y)
    return Max_x,Max_y

def findMin (road):
    Min = 9999

    for i in range(1,n+1):
        for j in range (1,n+1):
            if road[i][j] < Min:
                Min = road[i][j]
                Min_x = i
                Min_y = j

    #print(road[Min_x][Min_y],Min_x,Min_y)
    return Min_x,Min_y

def findGoal(x,y,road) :
    #time.sleep(1)
    #print(x,y,road[x][y])
    #printGoal(road)
    global cnt
    
    if x == Max_x and y == Max_y:
        #print("################################")
        cnt+=1
        return
    #길 지나옴
    
    ##상
    if road[x-1][y] > road[x][y]:
        findGoal(x-1,y,road)
    ##하
    if road[x+1][y] > road[x][y]:
        findGoal(x+1,y,road)
    ##좌
    if road[x][y-1] > road[x][y]:
        findGoal(x,y-1,road)

    ##우
    if road[x][y+1] > road[x][y]:
        findGoal(x,y+1,road)


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
    a.append([1]*n)
    for i in range (n):
        a.append(list(map(int,input().split())))

    for i in a:
        i.insert(0,1)
        i.append(1)
    a.append([1]*(n+2))

    global cnt
    cnt = 0
    
    
    #printGoal(a)
    Max_x,Max_y = findMax(a)
    Min_x,Min_y = findMin(a)
    
    findGoal(Min_x,Min_y,a)
    print(cnt)
    
                

    
#################################################################
    #print(n,a,sep='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


