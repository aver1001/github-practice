'''


'''
import sys
import time
def DFE(x,y,Sum) :
    #print(x,y,Sum)
    global Min
    if Sum+a[x][y] > Min:
        return
    if x == n-1 and y == n-1:
        #print(Sum+a[x][y])
        Min = Sum+a[x][y]
        return
    else:
        if x+1 != n:
            DFE(x+1,y,Sum+a[x][y])
        if y+1 != n:
            DFE(x,y+1,Sum+a[x][y])


    

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
    global Min
    Min = 9999
    for i in range (n):
        a.append(list(map(int,input().split())))
    
    DFE(0,0,0)
    print(Min)
                

    
#################################################################
    #print(n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


