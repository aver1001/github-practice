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
    n,m = map(int,(input().split()))
    a = list(map(int,(input().split())))

    #print(a)
    pt = 0
    target = m
    cnt = 0
    while(a):
        #print(a[pt],pt,target,cnt)
        if a[pt] == max(a):
            if target == pt:
                print(cnt+1)
                break
            else :
                a.pop(pt)
                cnt+=1
                pt-=1
                if target > pt:
                    target -=1
            
        if pt >= len(a)-1:
            pt = 0
        else:
            pt+=1

    
#################################################################
    #print(n,m,a,sep = ', ')
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


