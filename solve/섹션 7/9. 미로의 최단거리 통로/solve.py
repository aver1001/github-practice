'''


'''
import sys
import time
def printGoal(road) :
    for i in road:
        print(i)
    
def findGoal(x,y,road,distance) :
    #print(x,y,distance)
    #printGoal(road)
    global mins
    if distance > mins:
        return
    
    if x == 7 and y == 7:
        if mins > distance :
            mins = distance
        else :
            return
    #길 지나옴
    
    ##상
    if road[x-1][y] == 0:
        road[x-1][y] = 2
        findGoal(x-1,y,road,distance+1)
    ##하
    if road[x+1][y] == 0:
        road[x+1][y] = 2
        findGoal(x+1,y,road,distance+1)
    ##좌
    if road[x][y-1] == 0:
        road[x][y-1] = 2
        findGoal(x,y-1,road,distance+1)
    ##우
    if road[x][y+1] == 0:
        road[x][y+1] = 2
        findGoal(x,y+1,road,distance+1)
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    a = list()
    a.append([1]*7)
    for i in range (7):
        a.append(list(map(int,input().split())))
    for i in a:
        i.insert(0,1)
        i.append(1)
    a.append([1]*9)

    a[1][1] = 2

    #printGoal(a)

    global mins
    mins = 9999
    
    findGoal(1,1,a,0)
    if mins == 9999:
        mins = -1
    
#################################################################
    print(mins)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


