'''


'''
import sys
import time
def DFS (f,res,hap):
    global cnt

    if f == k:
        if hap % m == 0:
            cnt +=1
        return
    else:
        
        for i in range (res,n):
            DFS(f+1,i+1,hap+a[i])
        

    

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())

    cnt = 0
    DFS(0,0,0)


#################################################################
    print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


