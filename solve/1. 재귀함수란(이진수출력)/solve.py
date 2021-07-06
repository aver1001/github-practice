'''


'''
import sys
import time

def binary(x):
    if x == 1:
        result.insert(0,'1')
        return result
    else :
        result.insert(0,str(x%2))
        binary(x//2)
        
        
start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    result = list()
    binary(n)

    print(''.join(result))
    
    
                

    
#################################################################
    print()
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


