'''


'''
import sys
import time

def DFE(v,res):
    global cnt,maxs
    if v == n-1:
        if cnt > maxs:
            print(maxs,"=>",cnt)
            maxs = cnt
        return
    if a[v+1] > a[v]:
        cnt+=1
        DFE(v+1,a[v])
        cnt-=1
    DFE(v+1,res)


start = time.time()
for sn in range (1,3):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list(map(int,input().split()))
    global cnt,maxs
    maxs = 0
    cnt = 1
    DFE(0,0)
                

    
#################################################################
    print(n,a,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


