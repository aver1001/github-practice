'''


'''
import sys
import time
import copy
#sys.setrecursionlimit(10**6)

def printGoal(road) :
    
    for i in road:
        print(i)

def move(x,y) :
    
    a[x][y] = 3

    if y-1 !=-1:
        if a[x][y-1] == 1:
            return x,y-1
        ##우
    if y+1 != 10:
        if a[x][y+1] == 1:
            return x,y+1
        
        ##상
    if x-1 != -1:
        if a[x-1][y] == 1:
            return x-1,y






def startPoint(arr):
    return 9,arr[9].index(2)
                    
def ladder(arr) :
    x,y = startPoint(arr)

    while (x != 0) :
        #print(x,y)
        #printGoal(arr)
        
        x,y = move(x,y)
    print(y)
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    a = list()
    for i in range (10):
        a.append(list(map(int,input().split())))

        
    ladder(a)
    


    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


