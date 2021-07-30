'''


'''
import sys
import time
'''
def DEF (a):
    global cnt
    if a == 0:
        cnt +=1
        return
    if a < 0:
        return
    DEF(a-1)
    DEF(a-2)
'''
'''
def DFE(a):

    if a == 1 or a == 2:
        return a
    else:
        return DFE(a-1)+DFE(a-2)
    
'''
        

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
    
    for i in range (n):
        if i == 0 or i == 1:
            result.append(i+1)
        else:
            result.append(result[i-2]+result[i-1])

    print(result[-1])



    
                

    
#################################################################
    #print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


