'''


'''
import sys
import time

def DFS(x,st) :
    global cnt
    if x == m:
        for i in st:
            print(i,end = ' ')
        print()
        cnt +=1
        return
    
    for i in range (1, n+1):
        try:
            st.index(str(i))
        except:
            DFS(x+1,st+str(i))
        
        


start = time.time()
for sn in range (1,3):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,m = map(int,input().split())
    global cnt
    cnt = 0
    DFS(0,'')
    print(cnt)

        
        

    
#################################################################
    #print(a,n,m)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


