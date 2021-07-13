'''


'''
import sys
import time
def DEF(hap,days):
    global max
    #print(days, hap)
    if max < hap :
            max = hap
    if days > n-1:
        return
    ## 일할경우
    if (days+a[days][0]) <= n:
        DEF(hap+a[days][1],days+a[days][0])
    ## 일 안할경우 
    DEF(hap, days+1)

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list()
    for i in range(n):
        a.append(list(map(int,input().split())))

    global max
    max = 0
    DEF(0,0)

        
                

    
#################################################################
    print(max)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


