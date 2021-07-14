'''


'''
import sys
import time
def DEF(v,hap) :
    global cnt
    #print(v,hap)

    if hap > t:
        return
    if v == k:
        if hap == t:
            cnt +=1
    else:
        for i in range(a[v][1]+1):
            #print(i,a[v][1])
            DEF(v+1,hap+(a[v][0]*i))

 

start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    t = int(input())
    k = int(input())
    a = list()
    temp = list()
    global cnt
    cnt = 0
    for i in range(k):
         a.append(list(map(int,(input().split()))))

    DEF(0,0)
    print(cnt)

    
#################################################################
    #print(t,k,a,sep='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


