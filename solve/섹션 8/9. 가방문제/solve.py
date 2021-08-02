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
    n,m= map(int,(input().split()))
    a = list()
    for i in range (n):
        a.append(list(map(int,(input().split()))))
    result = [0]*(m+1)

    for i in a:
        #print(i)
        for j in range(i[0]+1,m+2):
            res = i[1]+ result[j-i[0]-1]
            if result[j-1] < res:
                result[j-1] = res
            #print(result)
            
            '''
            print(j, i[1],result[(j-1) %i[0]],j-i[0]-1)
            
            res = i[1]+ result[j-i[0]-1]
            if result[j-1] < res:
                result[j-1] = res
            print(result)
            '''

    print(max(result))
            
            
        
    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


