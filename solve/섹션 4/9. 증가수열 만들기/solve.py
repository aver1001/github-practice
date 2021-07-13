'''


'''
import sys
import time

start = time.time()
for sn in range (1,3):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n = int(input())
    a = list(map(int,input().split()))

    print(a)
    lt,rt = 0,n-1
    before = 0
    res = ""
    tmp = []
    while(lt <= rt):
        print(a[lt],a[rt])
        if a[lt] > before :
            tmp.append((a[lt],'L'))
        if a[rt] > before :
            tmp.append((a[rt],'R'))

        tmp.sort()
        if len(tmp) == 0:
            break
        else :
            res = res+tmp[0][1]
            before = tmp[0][0]
            if tmp[0][1] == 'L':
                lt +=1
            else :
                rt -=1
        tmp.clear()
    print(len(res),res)
    
#################################################################
    
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


