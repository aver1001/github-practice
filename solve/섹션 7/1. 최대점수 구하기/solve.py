'''


'''
import sys
import time
def DFS (v,choose,times):
    global max
    if times > m:
        return
    
    if v == n:
        temp = 0
        for i in range(n):
            if choose[i] == 1:
                temp += a[i][0]
        if max < temp:
            max = temp
        return

    ## 0
    choose.append(0)
    DFS(v+1,choose,times)
    choose.pop()
    ## 1
    choose.append(1)
    choose[v] = 1
    DFS(v+1,choose,times + a[v][1])
    choose.pop()
    
'''
def DFS (v,times,hap,choose):
    global max
    #print (hap,choose)
    if v == n:
        return
    for i in range (n):
        if choose[i] == 1:
                continue
        if times+a[i][1] > m:
            if max < hap:
                max = hap
            continue
        choose[i] = 1
        DFS(v+1,times+a[i][1],hap+a[i][0],choose)
        choose[i] = 0
'''
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,m = map(int,input().split())
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))

    global max
    max = 0

    
    DFS(0,list(),0)
    '''
    choose = [0]*n
    DFS(0,0,0,choose)
    '''
    print(max)

    
#################################################################
    #print(n,m,a,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


