'''


'''
import sys
import time


start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,k = map(int,input().split())
    queue = list()
    for i in range(1,n+1):
        queue.append(i)
    #print(n,k)
    cnt = 0
    while(queue):
        cnt +=k
        #print(queue,cnt,k)
        while( cnt > len(queue)):
            cnt -= len(queue)
        temp = queue.pop(cnt-1)
        cnt = cnt-1
        #print(temp,end = ' => ')

        
    print(temp)
    
#################################################################
    #print(n,k)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


