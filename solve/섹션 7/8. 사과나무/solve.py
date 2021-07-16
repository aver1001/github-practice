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
    a = list()
    for i in range (n):
        a.append(list(map(int,input().split())))

    lt,rt = n//2, n//2+1
    result = 0
    for j in range (n//2):
        #print(a[j][lt:rt],a[n-j-1][lt:rt],sep = '\n')
        result += sum(a[j][lt:rt])
        result += sum(a[n-j-1][lt:rt])
        lt -= 1
        rt += 1
    result += sum(a[n//2])
    print(result)

        
                

    
#################################################################
    #print(n,a,sep = '\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


