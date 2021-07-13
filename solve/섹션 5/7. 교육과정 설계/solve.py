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
    temp = list(input())
    n = int(input())
    
    
    for i in range(n):
        process = list(input())
        denial = list(temp)
        denial.pop(0)
        #print(process)
        for j in process:
            #print(j,denial)
            if denial:
                if j == denial[0]:
                    denial.pop(0)
            if j in denial:
                break
            
        if len(denial) == 0 :
            print("#",i+1," YES",sep = '')
        else:
            print("#",i+1," NO",sep = '')
        
                


    '''
    for i in range(n):
        process = list(input())
        print(process)
        waitting = temp
        waitting.append('4')
        need = list()
        need.append(waitting.pop(0))
        
        while(cnt != len(process)):
            print(process,process[cnt],cnt,need)
            if process[cnt] == waitting[0]:
                need.append(waitting.pop(0))
            try: ## 올바르지 않은 순서 
                waitting.index(process[cnt])
                
                print("#",i," NO",sep = '')
                break
            except:##올바른 순서 
                cnt += 1
                
            if cnt == len(process):
                print("#",i," YES",sep = '')
        cnt = 0
    '''          
                

    
#################################################################
    print()
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


