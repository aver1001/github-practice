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
    result = [0 for i in range (n)]
    #print(a,result)
    cnt = 0
    for i in range (n):
        cnt = 0
        for j in range (n):
            #print(j)
            if result[j] == 0:
                cnt +=1
            if cnt -1  == a[i]:
                #print("insert",i+1,i)
                result[j] = i+1
                break
    for i in result:
        print(i,end = ' ')
        
                

    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


