'''


'''
import sys
import time


start = time.time()
for sn in range (1,2):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n, m = map(int,input().split())
    result = list()
    for i in range (n):
        result.append([999]*n)
    for i in range (m):
        a,b,c= map(int,(input().split()))
        result[a-1][b-1] = c
    for i in range (6):
        result[i][i] = 0

    for i in result: print(i)

    print("#################")
    
    for k in range (n):
        for i in range (n):
            for j in range (n):
                #print(result[i][j],result[i][j],result[i][k]+result[k][j])
                result[i][j] = min(result[i][j],result[i][k]+result[k][j])




    for i in result: print(i)
                
    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


