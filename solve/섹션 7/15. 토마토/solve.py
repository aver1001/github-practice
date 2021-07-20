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
        i.insert(0,-1)
        i.append(-1)
        
    arr.insert(0,[-1]*(n+2))
    arr.insert(n+1,[-1]*(n+2))

    return arr

def isInZero(arr):

    for i in arr:
        if i.count(0) != 0:
            return True

    return False
            

def move() :
    temp = copy.deepcopy(a)

    for i in range (1,m+1):
        for j in range (1,n+1):
            if temp[j][i] == 1:
                try:
                ##상
                    if a[j-1][i] == 0: a[j-1][i] = 1
                    ##하
                    if a[j+1][i] == 0: a[j+1][i] = 1
                    ##좌
                    if a[j][i-1] == 0: a[j][i-1] = 1
                    ##우
                    if a[j][i+1] == 0: a[j][i+1] = 1
                except:
                    return False
            
                    
    
        
start = time.time()
for sn in range (1,2):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    m, n = map(int,(input().split()))
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))
    a = addNone(a)
    #printGoal(a)
    #print(m,n)
    cnt = 0
    while(isInZero(a)):
        #print(cnt)
        if cnt == m+n-2:
            break
        cnt+=1
        print(cnt)
        printGoal(a)
        if move() == False:
            cnt = -1
            break
        
    print(cnt)


    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


