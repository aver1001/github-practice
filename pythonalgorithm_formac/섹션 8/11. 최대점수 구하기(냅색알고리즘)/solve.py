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
    n, m = map(int,input().split())
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))

    result = [0]*(m+1)

    for i in a:
        for j in range(m,i[1]-1,-1):
            if result[j] < i[0]+result[j-i[1]]:
                result[j] = i[0]+result[j-i[1]]
            #print(result,i)
            
            

    
    
    
    
                

    
#################################################################
    print(result[-1])
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


