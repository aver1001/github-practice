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

    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    
    cnt = 0
    
    while (1):
        try :
            light_person = a.pop(0)
            cnt +=1
            for i in range (len(a)):
                #print(light_person,a[-(i+1)],)
                if light_person + a[-(i+1)] <= m:
                    heavy_person = a.pop(-(i+1))
                    #print(light_person,heavy_person)
                    #print(a)
                    break
        except:
            break
            
        
    print(cnt)
        
#################################################################
    #print(n,m,a,sep='\n')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


