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
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())

    result = [0]*(m+1)

    for i in a:
        for j in range (i,m+1):
            if result[j] >= 1 + result[j-i] or result[j] == 0:
                result[j] = 1+result[j-i]

                

    
#################################################################
    print(result[-1])
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


