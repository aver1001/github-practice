'''


'''
import sys
import time
import heapq as hq

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    a=[]
    while True:
        n=int(input())
        if n==-1:
            break
        if n==0:
            if len(a)==0:
                print(-1)
            else:
                print(hq.heappop(a))
        else:
            hq.heappush(a, n)
#################################################################
    print()
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


