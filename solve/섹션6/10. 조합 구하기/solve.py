'''


'''
import sys
import time
def DEF (v,res) :
    
    global result

    if v == m:
        temp = list()
        for i in res:
            temp.append(i)
        result.append(temp)
        return
    for i in a:
        #print(res,i)
        try :
            ## 이미 있는 값일경우
            res.index(str(i))
        except :
            ## 없는 값 일경우 
            DEF(v+1,res+str(i))
        

start = time.time()
for sn in range (5,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    n,m = map(int,(input().split()))
    a = list()
    global result
    result = list()

    for i in range (1,n+1):
        a.append(i)
    DEF(0,'')

    for i in range (len(result)):
        result[i].sort()
    result.sort()
    for i in result:
        temp = result.count(i)
        if result.count(i) >=2:
            for j in range(temp-1):
                result.remove(i)
                
    for i in result:
        for j in range(m):
            print(i[j],end=' ')
        print()
    print(len(result))
    
#################################################################

#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


