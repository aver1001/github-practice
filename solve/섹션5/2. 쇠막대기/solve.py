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
    a  = list(input())
    cnt = 0
    stack = list()
    for i in range (len(a)):
        
        if a[i] == '(':
            stack.append(['(',1])
        elif a[i] == ')':
            if a[i-1] == '(' :##raser
                #print("raser")
                stack.pop(-1)
                for j in range (len(stack)):
                    #print(stack, j, stack[j][1])
                    stack[j][1] += 1
                    
            else :
                temp = (stack.pop(0))[1]
                cnt += temp
                #print('닫힘',temp)
        #print(a[i],stack)
    
    
    
#################################################################
    print(cnt)
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    


