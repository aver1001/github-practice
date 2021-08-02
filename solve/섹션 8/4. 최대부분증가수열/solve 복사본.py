'''


'''
import sys
import time

def DFE(v):
    #print(result,v)
    if v == -1:
        #print(result,max(result))
        return

    if v == n-1:
        #print("First")
        result[v] = 1
        DFE(v-1)
    else:
        #자신보다 크고, 최대인것을 찾아 자신의 값으로 설정
        maxs = 0
        for i in range(v+1,n):
            ##자신보다 크다면
            if a[i] > a[v]:
                if maxs < result[i]:
                    maxs = result[i]
        result[v] = maxs + 1
        DFE(v-1)
                

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list(map(int,input().split()))
    result = [0]*n
    DFE(n-1)

    
#################################################################
    print(max(result))
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


