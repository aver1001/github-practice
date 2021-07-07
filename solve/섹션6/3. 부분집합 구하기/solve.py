'''


'''
import sys
import time

def DFS(x):

    if x == n+1:
        for i in range (1, n+1):
            if ch[i] == 1:
                print(i,end = ' ')
        print("")
    else :
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0
        DFS(x+1)
        
    

start = time.time()
for sn in range (1,2):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    ch=[0]*(n+1)
    DFS(1)
    
    
                

    
#################################################################
    print(n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


