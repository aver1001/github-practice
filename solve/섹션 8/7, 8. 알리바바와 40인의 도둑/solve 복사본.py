'''


'''
import sys
import time
def DFE() :
    
    for i in range (n):
        for j in range(n):
            if i== 0:
                if j == 0:
                    continue
                else :
                    a[i][j] += a[i][j-1]
            else:
                if j == 0:
                    a[i][j] += a[i-1][j]
                else:
                    a[i][j] += min(a[i-1][j],a[i][j-1])

    print(a[n-1][n-1])

    

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

    for i in range (n):
        a.append(list(map(int,input().split())))
    DFE()

    
    

                

    
#################################################################
    #print(n)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


