'''


'''
import sys
import time
def DFS (v):
    global cnt, path
    #print(path)
    
    if path.count(n) != 0 :
        cnt +=1
        '''
        for x in path:
            print(x, end = ' ')
        print()
        '''
        return

    
    if v == 0:
        path.append(1)
    for i in a:
        if i[0] == path[-1] and path.count(i[1]) == 0:
            path.append(i[1])
            DFS(v+1)
            path.pop()
    

            
                
    


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
    for i in range (m):
        a.append(list(map(int,input().split())))

    a.sort()
    global path
    path = list()
    cnt = 0
    DFS(0)
            
        
                
    print(cnt)
    
#################################################################
    #print(n,m)
    #print(a)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


