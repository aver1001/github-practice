'''


'''
import sys
import time

def DFS(x):
    #print(x)
    
    if x == n+1:
        First = 0
        Second = 0
        for i in range (1,n+1):
            if ch[i-1] == 1:
                First += a[i-1]
            else:
                Second += a[i-1]
        if First == Second :
            print("YES")
            sys.exit(0)
            
    else :      
        ch[x-1] = 1
        DFS(x+1)
        ch[x-1] = 0
        DFS(x+1)
    
start = time.time()
for sn in range (5,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list(map(int,input().split(' ')))
    ch =[0]*(n+1)
    DFS(1)
    print("NO")

    
                

    
#################################################################
    #print(n,a)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


