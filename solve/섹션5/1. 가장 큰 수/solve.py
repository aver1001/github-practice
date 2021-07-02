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
    ## n =
    a,n = map(int,(input().split()))
    a = list(str(a))
    lenth = len(a)- n
    #print(a,n)
    result = str()
    for i in range (1,lenth):
        index = a.index(max(a[:-(lenth-i)]))
        result += str(a[index])
        #print(a[:-(lenth-i)],a[index])
        a.pop(index)
        a = a[index:]

    result += str(a[0])
    print(result)
                

    
#################################################################
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


