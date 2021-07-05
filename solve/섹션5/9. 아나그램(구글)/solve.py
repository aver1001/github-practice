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
    a = input()
    b = input()
    result_a = list()
    result_b = list()
    for i in a:
        try:
            result_a[result_a.index(i)][1] +=1
        except:
            result_a.append((i,1))
        #print(result_a)

    for i in b:
        try:
            result_b[result_b.index(i)][1] +=1
        except:
            result_b.append((i,1))
        #print(result_b)

    result_a.sort()
    result_b.sort()

    if result_a == result_b :
        print("YES")
    else :
        print("NO")

    
#################################################################
    #print(a,b)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


