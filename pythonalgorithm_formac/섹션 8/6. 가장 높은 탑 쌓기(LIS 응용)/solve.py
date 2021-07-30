'''


'''
import sys
import time
def DFE(v):
    #print(result)
    if v == n: return
    if v == 0:
        result[v] = a[v][1]
        DFE(v+1)
    else:
        Max = 0
        for i in range (0,v):
            ##아래가 더 무거울 경우
            #print(a[i][2] ,"<", a[v][2])
            if a[i][2] < a[v][2]:
                #print(Max,"<",result[i])
                if Max < result[i]:
                    #print(Max, "=>",result[i])
                    Max = result[i]
            ##아래가 더 가벼울 경우
        #print("insert",a[v][1]+Max)
        result[v] = a[v][1]+Max
        DFE(v+1)

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
    result = [0]*n
    for i in range (n):
        a.append(list(map(int,input().split())))
    a.sort()
    DFE(0)

    print(max(result))
    
#################################################################
    #print(n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


