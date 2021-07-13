'''


'''
import sys
import time
def DEF (v,hap) :
    global result
    result.append(hap)
    
    if v == k:
        return
    else:
        ## 더하기 
        DEF(v+1,hap+a[v])
        ## 빼기
        DEF(v+1,hap-a[v])
        ## 그냥진행
        DEF(v+1,hap)

def impossible():
    temp = [0]*sum(a)
    
    for i in result:
        if i < 0:
            continue
        if temp[i-1] == 0:
            temp[i-1] = 1

    return temp.count(0)
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    k = int(input())
    a = list(map(int,input().split()))
    global result
    result = list()
    DEF(0,0)
                
    result.sort()
    
    print(impossible())
#################################################################
    #print(k,a)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


